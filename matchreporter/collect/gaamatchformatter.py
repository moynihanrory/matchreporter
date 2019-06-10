from matchreporter.constants import FIRST_HALF_START, FIRST_HALF_END, SECOND_HALF_START, SECOND_HALF_END, FORMAT_ROW_TIME, \
    FORMAT_ROW_HALF, FORMAT_ROW_SECTOR, FORMAT_ROW_EVENT, FORMAT_ROW_TEAM, FORMAT_ROW_LOCATION, FORMAT_ROW_PLAYER, \
    LOCATION_TAG, EVENT_ENDING
from matchreporter.helpers.pitchgrid import Grid
from matchreporter.helpers.stringhelper import stripAndConvertHalfToInt, stripAndConvertTimeToInt
from matchreporter.helpers.timesector import getTimeSector


def cleanAndFormatData(mobileAppOutput):
    firstHalfOn = False
    secondHalfOn = False
    isMatchOn = False
    grid = Grid()
    formattedLines = []

    for index, line in enumerate(mobileAppOutput):
        if isMatchOn is not True:
            if line.lower().startswith(FIRST_HALF_START.lower()):
                firstHalfOn = True
                isMatchOn = True
                continue

        if isMatchOn is True and firstHalfOn is True:
            if line.lower().startswith(FIRST_HALF_END.lower()):
                firstHalfOn = False
                continue

        if isMatchOn is True and firstHalfOn is False and secondHalfOn is False:
            if line.lower().startswith(SECOND_HALF_START.lower()):
                secondHalfOn = True
                continue

        if isMatchOn is True and firstHalfOn is False and secondHalfOn is True:
            if line.lower().startswith(SECOND_HALF_END.lower()):
                secondHalfOn = False
                isMatchOn = False
                continue

        if (isMatchOn and (firstHalfOn or secondHalfOn)):
            reFormattedLine = formatLine(line, grid)

            formattedLines.insert(len(formattedLines), reFormattedLine)

    return formattedLines


def formatLine(line, grid):
    lineChunks = line.split()

    totalChunks = len(lineChunks)

    time = stripAndConvertTimeToInt(lineChunks[0])

    half = stripAndConvertHalfToInt(lineChunks[1])

    team = lineChunks[3]

    location, locationEndIndex = extractLocation(lineChunks, totalChunks)

    pitchLocation = grid.getPitchSector(location)

    event, eventEndIndex = extractEvent(lineChunks, locationEndIndex)

    player = extractPlayer(lineChunks, eventEndIndex, locationEndIndex)

    sector = getTimeSector(time, half)

    row = {FORMAT_ROW_TIME: time,
           FORMAT_ROW_HALF: half,
           FORMAT_ROW_SECTOR: sector,
           FORMAT_ROW_TEAM: team,
           FORMAT_ROW_EVENT: event,
           FORMAT_ROW_PLAYER: player,
           FORMAT_ROW_LOCATION: pitchLocation}

    return row

def extractLocation(lineChunks, totalChunks):
    location = None

    if (LOCATION_TAG in lineChunks):
        location = lineChunks[totalChunks - 1]
    else:
        return None, totalChunks

    locationEndIndex = totalChunks - 1

    if location is not None:
        locationEndIndex = locationEndIndex - 1

    return location, locationEndIndex


def extractEvent(lineChunks, eventEndIndex):
    playerStringStart = None

    event = lineChunks[4]

    for i in range(5, eventEndIndex):
        event = event + ' ' + lineChunks[i]

        if (lineChunks[i].lower() in EVENT_ENDING):
            playerStringStart = i + 1

            break

    return event, playerStringStart


def extractPlayer(lineChunks, playerStartIndex, playerEndIndex):
    player = ''

    if playerStartIndex is None or playerEndIndex is None:
        return player

    for i in range(playerStartIndex, playerEndIndex):
        player = player + ' ' + lineChunks[i]

    return player


