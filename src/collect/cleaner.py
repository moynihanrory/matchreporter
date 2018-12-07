import src.constants
import src.helpers.timeHelper
from constants import TIDY_FULL_TIME


def tidyData(data):
    splitLines = []

    for index, line in enumerate(data):
        if (line.lower().startswith(TIDY_FULL_TIME.lower())):
            break

        if skipOrProcessLine(line, index):
            continue

        splitLine = line.split()

        splitLines.insert(len(splitLines), splitLine)


    return splitLines


def skipOrProcessLine(line, index):
    if index < src.constants.TIDY_SI: return src.constants.TIDY_SKIP
    if line == '': return src.constants.TIDY_SKIP
    if line.startswith(src.constants.TIDY_LS1): return src.constants.TIDY_SKIP
    if line.startswith(src.constants.TIDY_LS2): return src.constants.TIDY_SKIP
    if line.startswith(src.constants.TIDY_LS3): return src.constants.TIDY_SKIP
    if line.startswith(src.constants.TIDY_LS4): return src.constants.TIDY_SKIP
    if line.startswith(src.constants.TIDY_LS5): return src.constants.TIDY_SKIP
    if line.startswith(src.constants.TIDY_LS6): return src.constants.TIDY_SKIP
    if line.startswith(src.constants.TIDY_LS7): return src.constants.TIDY_SKIP
    if line.startswith(src.constants.TIDY_LS8): return src.constants.TIDY_SKIP
    if line.startswith(src.constants.TIDY_LS9): return src.constants.TIDY_SKIP

    return src.constants.TIDY_PROCESS


def formatData(data):
    formattedLines = []

    for index, line in enumerate(data):
        splitLineLength = len(line)

        if (splitLineLength == 0):
            continue

        if (line[0].lower().startswith(TIDY_FULL_TIME.lower())):
            break

        row = formatLine(line, splitLineLength)

        formattedLines.insert(len(formattedLines), row)

    return formattedLines


def formatLine(splitLine, splitLineLength):
    # update the half
    half = extractHalf(splitLine)
    time = extractTime(splitLine)
    sector = extractSector(half, time)
    team = extractTeam(splitLine)
    playerNumber = extractPlayerNumber(splitLine, splitLineLength)

    # if no player set we want to concat remain parts
    if (playerNumber is None or playerNumber == 0):
        playerNumber = 0
        stopIndex = splitLineLength
    else:
        stopIndex = splitLineLength - 1

    playerStringStart = 0
    event, playerStringStart = extractEvent(playerStringStart, splitLine, stopIndex)
    player = extractPlayer(playerNumber, playerStringStart, splitLine, stopIndex)

    row = {src.constants.FORMAT_ROW_TIME: time,
           src.constants.FORMAT_ROW_TIME_BUCKET: sector,
           src.constants.FORMAT_ROW_HALF: half,
           src.constants.FORMAT_ROW_TEAM: team,
           src.constants.FORMAT_ROW_ACTION: event,
           src.constants.FORMAT_ROW_PLAYER: player}

    return row


def extractPlayer(playerNumber, playerStringStart, splitLine, stopIndex):
    if (playerNumber == 0 and (playerStringStart > 0) and (playerStringStart < len(splitLine))):
        player = splitLine[playerStringStart]
        for i in range(playerStringStart + 1, stopIndex):
            player = player + ' ' + splitLine[i]
    else:
        if playerNumber != 0:
            player = str(playerNumber)
            return player


def extractEvent(playerStringStart, splitLine, stopIndex):
    event = splitLine[4]
    for i in range(5, stopIndex):
        event = event + ' ' + splitLine[i]
        if (splitLine[i] in src.constants.TIDY_EVENT_FROM):
            playerStringStart = i + 1
            break
    return event, playerStringStart


def extractPlayerNumber(splitLine, splitLineLength):
    playerNumber = src.helpers.timeHelper.parseInt(splitLine[splitLineLength - 1])
    return playerNumber


def extractTeam(splitLine):
    team = splitLine[3]
    return team


def extractSector(half, time):
    timeBucket = src.helpers.timeHelper.getTimeBucket(time, half)
    return timeBucket


def extractTime(splitLine):
    time = splitLine[0].strip(src.constants.TIDY_STR_MINS)
    return time


def extractHalf(splitLine):
    half = 1
    if splitLine[1].startswith(src.constants.TIDY_LS10):
        half = 2
    return half