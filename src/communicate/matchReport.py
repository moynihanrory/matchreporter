import pandas as pd
import stringBuilder
from constants import EX_SECTORS_SHEET_NAME, EX_HALVES_SHEET_NAME, EX_MATCH_SHEET_NAME
from fileHelper import getOutputFilename, createAbsoluteFilenameAndDirectory
from modes import getPrefix


class Report(object):
    def __init__(self, outputDir):
        self.outputDir = outputDir

    def generate(self, analysisList):
        absoluteFilename = self.createAbsoluteFilename(analysisList[0], self.outputDir)

        self.createExcelWorkbook(absoluteFilename, analysisList)

    def createExcelWorkbook(self, absoluteFilename, analysisList):
        writer = pd.ExcelWriter(absoluteFilename)

        for analysis in analysisList:
            analysis.match.to_excel(writer, sheet_name=self.getSheetName(analysis, EX_MATCH_SHEET_NAME))
            analysis.halves.to_excel(writer, sheet_name=self.getSheetName(analysis, EX_HALVES_SHEET_NAME))
            analysis.sectors.to_excel(writer, sheet_name=self.getSheetName(analysis, EX_SECTORS_SHEET_NAME))

        writer.save()

    def getSheetName(self, analysis, defaultName):
        sheet = stringBuilder.getSheetName(self.getSheetPrefix(analysis.source), defaultName)

        return sheet

    def getSheetPrefix(self, source):
        return getPrefix(source)

    def createAbsoluteFilename(self, analysis, outputDir):
        filename = getOutputFilename(analysis.teams)

        absoluteFilename = createAbsoluteFilenameAndDirectory(filename, outputDir)

        return absoluteFilename
