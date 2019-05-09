import os

from matchreporter.constants import EX_OUTPUT_AGG_DATA_FILE, EX_OUTPUT_REPORT_FILE, EX_OUTPUT_DIRECTORY, \
    MATCH_ANALYSIS_REPORT_TEMPLATE
from matchreporter.helpers.datetimehelper import getTodaysDate


def readFile(filename, mode='r'):
    with open(filename, mode) as inputFile:
        return inputFile.read()


def readTextFileAsLines(filename):
    return readFile(filename).splitlines()


def loadDataFromFile(absoluteFileName):
    return readTextFileAsLines(absoluteFileName)


def createOutputDirectory(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)


def createFilePath(filename, outputDir):
    createOutputDirectory(outputDir)

    return os.path.join(outputDir, filename)


def getOutputExcelFilename(teams):
    filename = EX_OUTPUT_AGG_DATA_FILE.format(teams[0], teams[1], getTodaysDate())

    return filename


def getReportExcelFilename(teams):
    filename = EX_OUTPUT_REPORT_FILE.format(teams[0], teams[1], getTodaysDate())

    return filename


def getOutputDirectoryName(teams):
    dirName = EX_OUTPUT_DIRECTORY.format(teams[0], teams[1], getTodaysDate())

    return dirName


def getMatchAnalysisReportName(outputDirectory):
    return os.path.join(outputDirectory, EX_OUTPUT_REPORT_FILE)


def getMatchAnalysisReportTemplateName():
    return os.path.join(os.getcwd(), MATCH_ANALYSIS_REPORT_TEMPLATE)