from datetime import datetime, date

from constants import MDB_IMPORT_FILE_SOURCE_TXT, MDB_IMPORT_FILE___TXT, MDB_DATETIME_FORMAT, EX_OUTPUT_REPORT_FILE, \
    MDB_DATE_FORMAT


def createSource():
    return MDB_IMPORT_FILE_SOURCE_TXT


def createImportTxtFilename():
    datestring = datetime.strftime(datetime.now(), MDB_DATETIME_FORMAT)

    filename = MDB_IMPORT_FILE___TXT.format(datestring)

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