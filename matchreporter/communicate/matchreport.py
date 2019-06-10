import os
from pathlib import Path
from pandas import ExcelWriter

from matchreporter.constants import EX_MATCH_SHEET_NAME, EX_PLAYERS_SHEET_NAME_1, EX_PLAYERS_SHEET_NAME_2, \
    EX_HALVES_SHEET_NAME, EX_LOCATIONS_SHEET_NAME_1, EX_LOCATIONS_SHEET_NAME_2, EX_SECTORS_SHEET_NAME, \
    EX_SECTORS1_SHEET_NAME, EX_SECTORS2_SHEET_NAME, EX_POSSESSIONS_SHEET_NAME, EX_TACKLES_SHEET_NAME, EX_RAW_SHEET_NAME
from matchreporter.helpers.filehelper import getGaaMatchOutputExcelFilename, getOutputDirectoryName, createFilePath, \
    getGaaMatchReportTemplateName, getSportscodeReportTemplateName, \
    getSportscodeOutputExcelFilename, getSportsCodeAnalysisReportName, getGaaMatchAnalysisReportName



def createMatchReport(outputLocation, analysis, sportsCodeOutput):
    outputFilename, outputDirectory = createOutputFilename(outputLocation, analysis, sportsCodeOutput)

    createGeneratedDataExcelWorkbook(outputFilename, analysis)

    outputReport = generateReportFromTemplate(outputDirectory, sportsCodeOutput)

    return outputReport


def createGeneratedDataExcelWorkbook(absoluteFilename, analysis):
    writer = ExcelWriter(absoluteFilename)

    analysis.raw.to_excel(writer, sheet_name=EX_RAW_SHEET_NAME)
    analysis.match.to_excel(writer, sheet_name=EX_MATCH_SHEET_NAME)
    analysis.players1.to_excel(writer, sheet_name=EX_PLAYERS_SHEET_NAME_1)
    analysis.players2.to_excel(writer, sheet_name=EX_PLAYERS_SHEET_NAME_2)
    analysis.halves.to_excel(writer, sheet_name=EX_HALVES_SHEET_NAME)
    analysis.sectors.to_excel(writer, sheet_name=EX_SECTORS_SHEET_NAME)
    analysis.sectors1.to_excel(writer, sheet_name=EX_SECTORS1_SHEET_NAME)
    analysis.sectors2.to_excel(writer, sheet_name=EX_SECTORS2_SHEET_NAME)

    if analysis.location1 is not None:
        analysis.location1.to_excel(writer, sheet_name=EX_LOCATIONS_SHEET_NAME_1)

    if analysis.location2 is not None:
        analysis.location2.to_excel(writer, sheet_name=EX_LOCATIONS_SHEET_NAME_2)

    if analysis.possessions is not None:
        analysis.possessions.to_excel(writer, sheet_name=EX_POSSESSIONS_SHEET_NAME)

    if analysis.tackles is not None:
        analysis.tackles.to_excel(writer, sheet_name=EX_TACKLES_SHEET_NAME)

    writer.save()


def createOutputFilename(outputDir, analysis, sportsCodeOutput):
    filename = None

    if sportsCodeOutput is True:
        filename = getSportscodeOutputExcelFilename(analysis.teams)
    else:
        filename = getGaaMatchOutputExcelFilename(analysis.teams)

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


def generateReportFromTemplate(outputDirectory, sportsCodeOutput):
    template = None
    report = None

    if sportsCodeOutput is True:
        template = Path(getSportscodeReportTemplateName())
        report = Path(getSportsCodeAnalysisReportName(outputDirectory))
    else:
        template = Path(getGaaMatchReportTemplateName())
        report = Path(getGaaMatchAnalysisReportName(outputDirectory))

    if template is not None:
        report.write_bytes(template.read_bytes())

    return report.as_posix()


