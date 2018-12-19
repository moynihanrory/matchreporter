import sys
import logging
import argparse
from matchReport import Report
from typeFactory import TypeFactory
from modes import MODES

def parseCommandLine():
    parser = argparse.ArgumentParser()

    parser.add_argument("-g", help="The full path and filename of export from GAAMatch")
    parser.add_argument("-x", help="The full path and filename of the SportsCode XML")
    parser.add_argument("-r", help="The report output file name and location")

    args = parser.parse_args()

    return args

def main(argv):
    args = parseCommandLine()

    objectFactory = TypeFactory(args)

    analysisList = []

    for mode in MODES:
        objectFactory.setOperatingMode(mode)

        collector = objectFactory.getCollector()

        if collector is None:
            continue

        cleaned = collector.cleanAndImportData()

        transformer = objectFactory.getTransformer()

        transformedData = transformer.transform(cleaned)

        analyiser = objectFactory.getAnalyzer()

        analysis = analyiser.analyze(transformedData)

        analysisList.append(analysis)

    report = Report(args.r)

    report.generate(analysisList)

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)

    main(sys.argv[1:])
