import os
import xmltodict
from constants import FILE_REL_OUTPUT_DIRECTORY
from stringBuilder import createOutputExcelFilename

def readFile(filename, mode='r'):
    with open(filename, mode) as inputFile:
        return inputFile.read()

def readTxtFile(filename):
    return readFile(filename).splitlines()

def readXmlFile(filename):
    xmlString = readFile(filename, mode='rb')

    return xmltodict.parse(xmlString)

def getExcelFilename(teams):
    return getOutputFilename(teams)

def getOutputFilename(teams):
    excelfilename = createOutputExcelFilename(teams)

    return excelfilename

def getOutputImageAbsFilename(filename):
    return FILE_REL_OUTPUT_DIRECTORY + filename.lower()

def createOutputDirectory(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)

def createAbsoluteFilenameAndDirectory(filename, outputDir):
    createOutputDirectory(outputDir)

    return os.path.join(outputDir, filename)