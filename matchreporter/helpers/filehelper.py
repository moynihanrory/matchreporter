import os

from matchreporter.constants import EX_GAAMATCH_OUTPUT_AGG_DATA_FILE, EX_GAAMATCH_OUTPUT_REPORT_FILE, EX_OUTPUT_DIRECTORY, \
    GAAMATCH_ANALYSIS_REPORT_TEMPLATE, SPORTSCODE_REPORT_TEMPLATE, EX_SPORTSCODE_OUTPUT_AGG_DATA_FILE, \
    EX_SPORTSCODE_OUTPUT_REPORT_FILE
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


def getGaaMatchOutputExcelFilename(teams):
    filename = EX_GAAMATCH_OUTPUT_AGG_DATA_FILE.format(teams[0], teams[1], getTodaysDate())

    return filename


def getGaaMatchReportExcelFilename(teams):
    filename = EX_GAAMATCH_OUTPUT_REPORT_FILE.format(teams[0], teams[1], getTodaysDate())

    return filename


def getSportscodeOutputExcelFilename(teams):
    filename = EX_SPORTSCODE_OUTPUT_AGG_DATA_FILE.format(teams[0], teams[1], getTodaysDate())

    return filename


def getSportscodeReportExcelFilename(teams):
    filename = EX_SPORTSCODE_OUTPUT_REPORT_FILE.format(teams[0], teams[1], getTodaysDate())

    return filename


def getOutputDirectoryName(teams):
    dirName = EX_OUTPUT_DIRECTORY.format(teams[0], teams[1], getTodaysDate())

    return dirName


def getGaaMatchReportTemplateName():
    return os.path.join(os.getcwd(), GAAMATCH_ANALYSIS_REPORT_TEMPLATE)


def getSportscodeReportTemplateName():
    return os.path.join(os.getcwd(), SPORTSCODE_REPORT_TEMPLATE)


def getGaaMatchAnalysisReportName(outputDirectory):
    return os.path.join(outputDirectory, EX_GAAMATCH_OUTPUT_REPORT_FILE)


def getSportsCodeAnalysisReportName(outputDirectory):
    return os.path.join(outputDirectory, EX_SPORTSCODE_OUTPUT_REPORT_FILE)