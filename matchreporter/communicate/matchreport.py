import os
from pathlib import Path
from pandas import ExcelWriter

from matchreporter.constants import EX_MATCH_SHEET_NAME, EX_PLAYERS_SHEET_NAME_1, EX_PLAYERS_SHEET_NAME_2, \
    EX_HALVES_SHEET_NAME, EX_LOCATIONS_SHEET_NAME_1, EX_LOCATIONS_SHEET_NAME_2, EX_SECTORS_SHEET_NAME
from matchreporter.helpers.filehelper import getOutputExcelFilename, getOutputDirectoryName, createFilePath, \
    getMatchAnalysisReportTemplateName, getMatchAnalysisReportName


def createMatchReport(outputLocation, analysis):
    outputFilename, outputDirectory = createOutputFilename(outputLocation, analysis)

    createGeneratedDataExcelWorkbook(outputFilename, analysis)

    outputReport = generateReportFromTemplate(outputDirectory)

    return outputReport


def createGeneratedDataExcelWorkbook(absoluteFilename, analysis):
    writer = ExcelWriter(absoluteFilename)

    analysis.match.to_excel(writer, sheet_name=EX_MATCH_SHEET_NAME)
    analysis.players1.to_excel(writer, sheet_name=EX_PLAYERS_SHEET_NAME_1)
    analysis.players2.to_excel(writer, sheet_name=EX_PLAYERS_SHEET_NAME_2)
    analysis.halves.to_excel(writer, sheet_name=EX_HALVES_SHEET_NAME)
    analysis.sectors.to_excel(writer, sheet_name=EX_SECTORS_SHEET_NAME)
    analysis.location1.to_excel(writer, sheet_name=EX_LOCATIONS_SHEET_NAME_1)
    analysis.location2.to_excel(writer, sheet_name=EX_LOCATIONS_SHEET_NAME_2)

    writer.save()


def createOutputFilename(outputDir, analysis):
    filename = getOutputExcelFilename(analysis.teams)

    outputDirectoryName = createOutputDirectory(analysis, outputDir)

    absoluteFilename = createFilePath(filename, outputDirectoryName)

    return absoluteFilename, outputDirectoryName


def createOutputDirectory(analysis, outputDir):
    if outputDir is None:
        outputDir = os.getcwd()

    outputDirectoryName = os.path.join(outputDir, getOutputDirectoryName(analysis.teams))

    if os.path.exists(outputDirectoryName) is False:
        os.mkdir(outputDirectoryName)

    return outputDirectoryName


def generateReportFromTemplate(outputDirectory):
    template = Path(getMatchAnalysisReportTemplateName())

    report = Path(getMatchAnalysisReportName(outputDirectory))

    report.write_bytes(template.read_bytes())

    return report.as_posix()


