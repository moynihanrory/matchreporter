import matchreport.constants
import matchreport.helpers.timehelper
from matchreport.constants import TIDY_FULL_TIME

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
    if index < matchreport.constants.TIDY_SI:
        return matchreport.constants.TIDY_SKIP

    if line == '':
        return matchreport.constants.TIDY_SKIP

    if line.startswith(matchreport.constants.TIDY_LS1):
        return matchreport.constants.TIDY_SKIP
    elif line.startswith(matchreport.constants.TIDY_LS2):
        return matchreport.constants.TIDY_SKIP
    elif line.startswith(matchreport.constants.TIDY_LS3):
        return matchreport.constants.TIDY_SKIP
    elif line.startswith(matchreport.constants.TIDY_LS4):
        return matchreport.constants.TIDY_SKIP
    elif line.startswith(matchreport.constants.TIDY_LS5):
        return matchreport.constants.TIDY_SKIP
    elif line.startswith(matchreport.constants.TIDY_LS6):
        return matchreport.constants.TIDY_SKIP
    elif line.startswith(matchreport.constants.TIDY_LS7):
        return matchreport.constants.TIDY_SKIP
    elif line.startswith(matchreport.constants.TIDY_LS8):
        return matchreport.constants.TIDY_SKIP
    elif line.startswith(matchreport.constants.TIDY_LS9):
        return matchreport.constants.TIDY_SKIP

    return matchreport.constants.TIDY_PROCESS

def formatData(data):
    formattedLines = []

    for line in data:
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

    row = {matchreport.constants.FORMAT_ROW_TIME: time,
           matchreport.constants.FORMAT_ROW_TIME_BUCKET: sector,
           matchreport.constants.FORMAT_ROW_HALF: half,
           matchreport.constants.FORMAT_ROW_TEAM: team,
           matchreport.constants.FORMAT_ROW_ACTION: event,
           matchreport.constants.FORMAT_ROW_PLAYER: player}

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

    return None

def extractEvent(playerStringStart, splitLine, stopIndex):
    event = splitLine[4]

    for i in range(5, stopIndex):
        event = event + ' ' + splitLine[i]

        if (splitLine[i] in matchreport.constants.TIDY_EVENT_FROM):
            playerStringStart = i + 1

            break

    return event, playerStringStart

def extractPlayerNumber(splitLine, splitLineLength):
    playerNumber = matchreport.helpers.timehelper.parseInt(splitLine[splitLineLength - 1])

    return playerNumber

def extractTeam(splitLine):
    team = splitLine[3]
    return team

def extractSector(half, time):
    if len(time) == 2 and time.startswith('0'):
        timeInt = matchreport.helpers.timehelper.parseInt(time, stripPrefix=True)
    else:
        timeInt = matchreport.helpers.timehelper.parseInt(time, stripPrefix=False)

    timeBucket = matchreport.helpers.timehelper.getTimeBucket(str(timeInt), half)

    return timeBucket

def extractTime(splitLine):
    time = splitLine[0].strip(matchreport.constants.TIDY_STR_MINS)

    return time

def extractHalf(splitLine):
    half = 1

    if splitLine[1].startswith(matchreport.constants.TIDY_LS10):
        half = 2

    return half