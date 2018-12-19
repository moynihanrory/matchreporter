from datetime import datetime
from matchreport.constants import EX_OUTPUT_REPORT_FILE, \
    EX_OUTPUT_REPORT_FILE_SHEET, MDB_IMPORT_FILE_TXT, MDB_IMPORT_FILE_SOURCE_TXT, \
    MDB_DATETIME_FORMAT, MDB_DATE_FORMAT


def createSource():
    return MDB_IMPORT_FILE_SOURCE_TXT

def createImportTxtFilename():
    datestring = datetime.strftime(datetime.now(), MDB_DATETIME_FORMAT)

    filename = MDB_IMPORT_FILE_TXT.format(datestring)

    return filename

def createTablename(prefix):
    filename = prefix.format(getDateTimeString())

    return filename

def createOutputExcelFilename(teams):
    filename = EX_OUTPUT_REPORT_FILE.format(teams[0], teams[1], getDateString())

    return filename

def getDateTimeString():
    datestring = datetime.strftime(datetime.now(), MDB_DATETIME_FORMAT)

    return datestring

def getDateString():
    datestring = datetime.strftime(datetime.now(), MDB_DATE_FORMAT)

    return datestring

def getSheetName(prefix, postfix):
    sheetName = EX_OUTPUT_REPORT_FILE_SHEET.format(prefix, postfix)

    return sheetName