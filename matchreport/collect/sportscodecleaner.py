import math
from datetime import timedelta
import matchreport.constants
import matchreport.helpers.timehelper
from matchreport.constants import TIDY_SCX_CODE, TIDY_SCX_OBS_1, TIDY_SCX_OBS_2, TIDY_SCX_OBS_3, TIDY_SCX_START, TIDY_SCX_END, \
    TIDY_SCX_UNDERSCORE, TIDY_SCX_OBS_TEAM_1, TIDY_SCX_OBS_TEAM_2

def tidyData(data):
    tidiedRows = []

    observations = data[TIDY_SCX_OBS_1][TIDY_SCX_OBS_2][TIDY_SCX_OBS_3]

    for row in observations:
        tidiedRows.append(row)

    return tidiedRows


def formatData(data):
    formattedLines = []
    _htReached = False

    lastRow = None

    for row in data:

        row, dropRow = formatRow(row, lastRow)

        if not dropRow:
            formattedLines.insert(len(formattedLines), row)

        lastRow = row

    return formattedLines


def formatRow(row, lastRow):
    # update the half
    time = extractTime(row)
    half = extractHalf(row, lastRow)
    sector = extractSector(half, time)
    team = extractTeam(row)

    event = extractEvent(row)

    row = {matchreport.constants.FORMAT_ROW_TIME: time,
           matchreport.constants.FORMAT_ROW_TIME_BUCKET: sector,
           matchreport.constants.FORMAT_ROW_HALF: half,
           matchreport.constants.FORMAT_ROW_TEAM: team,
           matchreport.constants.FORMAT_ROW_ACTION: event}

    return row, (team is None)


def extractTime(row):
    start = row[TIDY_SCX_START]

    end = row[TIDY_SCX_END]

    difference = float(end) - float(start)

    elapsed = float(start) + difference

    timeElapsed = str(timedelta(seconds=elapsed))

    return timeElapsed


def extractHalf(row, lastRow):
    if lastRow is None:
        return 1

    if lastRow[matchreport.constants.FORMAT_ROW_HALF] == 2:
        return lastRow[matchreport.constants.FORMAT_ROW_HALF]

    code = row[TIDY_SCX_CODE].upper().startswith(matchreport.constants.TIDY_SCX_OBS_HT)

    if (code):
        return 2

    return 1

def extractSector(half, time):
    timeString = time

    if half == 1:
        timeString = time[2:]
    elif half == 2 and timeString.startswith('0'):
        timeString = timeString[2:]

    t = time.split(':')

    totalMinutes = int(t[0]) * 60 + int(t[1]) * 1 + int(float(t[2])) / 60

    minute = str(math.ceil(totalMinutes))

    timeBucket = matchreport.helpers.timehelper.getTimeBucket(minute, half)

    return timeBucket

def extractTeam(row):
    code = row[TIDY_SCX_CODE].replace(' ', TIDY_SCX_UNDERSCORE)

    splitString = code.split(TIDY_SCX_UNDERSCORE)

    if splitString[0].upper().startswith(TIDY_SCX_OBS_TEAM_1.upper()) or splitString[0].upper().startswith(TIDY_SCX_OBS_TEAM_2.upper()):
        return splitString[0].upper()

    return None

def extractEvent(row):
    code = row[TIDY_SCX_CODE]

    splitString = code.split(TIDY_SCX_UNDERSCORE)

    if (len(splitString) == 2):
        return splitString[1].upper()

    return None
