import sys
import logging
import argparse

import reportBuilderFactory
import transformerFactory
import mongoManager
import collectorFactory
import sources
import analyzerFactory

def parseCommandLine():
    parser = argparse.ArgumentParser()
    importAppOutputGroup = parser.add_mutually_exclusive_group()
    importAppOutputGroup.add_argument("-f", "--importFile", help="The full path and filename", action="store_true")
    importAppOutputGroup.add_argument("-x", "--xml", help="The full path and filename", action="store_true")
    importAppOutputGroup.add_argument("-oid", "--objectId", help="The OID to retrieve and transform", action="store_true")
    parser.add_argument("fileOrId", action="store")
    parser.add_argument("-outputDir", action="store")
    args = parser.parse_args()
    return args


def main(argv):
    args = parseCommandLine()

    collector = collectorFactory.getCollectorForImportSource(sources.getSourceFromArgs(args))

    cleaned = collector.cleanAndImportData(args.fileOrId)

    transformer = transformerFactory.getTransformerForImportSource(sources.getSourceFromArgs(args))

    transformedData = transformer.transform(cleaned)

    analyiser = analyzerFactory.getAnalyzerForImportSource(sources.getSourceFromArgs(args))

    analysis = analyiser.analyze(transformedData)

    report = reportBuilderFactory.getReportBuilderForImportSource(sources.getSourceFromArgs(args))

    report.generate(analysis, transformer.mapping, args.outputDir)



if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)

    main(sys.argv[1:])



def generateAndPersist(argv):
    args = parseCommandLine()

    collector = collectorFactory.getCollectorForImportSource(sources.getSourceFromArgs(args))

    cleaned = collector.cleanAndImportData(args.fileOrId)

    cleanedDataOid = mongoManager.storeGaaMatchImportAndCleanedData(collector.getImportData(), cleaned)

    if cleanedDataOid is None:
        return  # error

    # data has been previously collected and ready for transformation
    if args.xml is False and (args.objectId or cleaned):
        # collect data
        cleanedData = collector.getCleanedDataById(cleanedDataOid)

        if cleanedData == None:
            return

        transformer = transformerFactory.getTransformerForImportSource(sources.getSourceFromArgs(args))

        transformedData = transformer.transform(cleanedData)

        transformedDataOid = mongoManager.storeMappingAndTransform(cleanedDataOid, transformedData,
                                                                   transformer.mapping)

    # now we want to perform analysis
    # ﻿ObjectId("5c06b38ec9799f177e410d43")
    if transformedData is not None:  # transformedDataOid is not None or
        transformedData = transformer.getTransformedDataById(transformedDataOid)

        if transformedData is None:
            return

        analyiser = analyzerFactory.getAnalyzerForImportSource(sources.getSourceFromArgs(args))

        analysis = analyiser.analyze(transformedData)

        report = reportBuilderFactory.getReportBuilderForImportSource(sources.getSourceFromArgs(args))

        report.generate(analysis, transformer.mapping, args.outputDir)


