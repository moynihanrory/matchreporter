import time
from xml.etree import ElementTree as ET

from matchreporter.constants import FORMAT_ROW_TIME, \
    FORMAT_ROW_HALF, FORMAT_ROW_SECTOR, FORMAT_ROW_EVENT, FORMAT_ROW_TEAM, FORMAT_ROW_LOCATION, FORMAT_ROW_PLAYER

from matchreporter.helpers.stringhelper import stripAndConvertTimeToInt
from matchreporter.helpers.timesector import getTimeSector


def cleanAndFormatData(filename):
    tree = ET.parse(filename)

    root = tree.getroot()

    flattened = flatten(root)

    rows = restructureRows(flattened)

    return rows


def flatten(xmlroot):
    instances = xmlroot.findall('.//instance')

    records = []

    for instance in instances:
        instance.getchildren()

        id = instance.find('ID')
        start = instance.find('start')
        end = instance.find('end')
        code = instance.find('code')
        labels = instance.findall('label')
        group = None
        text = None

        row = { 'id': id.text.lower(),
                'start': start.text.lower(),
                'end': end.text.lower(),
                'code': code.text.lower()
                }

        if labels is not None:
            for label in labels:
                label.getchildren()

                group = label.find('group')
                text = label.find('text')

                row.update({(group.text if group is not None else None).lower() : (text.text if text is not None else None).lower()})

        records.append(row)

    return records


def restructureRows(rows):
    firstHalfOn = False
    secondHalfOn = False
    isMatchOn = False
    firstHalfStart = 0
    secondHalfStart = 0
    restructuredRows = []

    for index, row in enumerate(rows):
        if isMatchOn is not True:
            if row['code'] == 'clock' and row['time'] == '1st start':
                firstHalfStart = stripAndConvertTimeToInt(row['start'])
                firstHalfOn = True
                isMatchOn = True
                continue

        if isMatchOn is True:
            if row['code'] == 'clock' and row['time'] == '2nd start':
                firstHalfOn = False
                secondHalfOn = True

                secondHalfStart = stripAndConvertTimeToInt(row['start'])
                firstHalfStart = 0
                continue

        if (isMatchOn and (firstHalfOn or secondHalfOn)):
            row = restructureRow(index, row, firstHalfOn, firstHalfStart, secondHalfOn, secondHalfStart)

            restructuredRows.append(row)

    return restructuredRows


def restructureRow(index, row, firstHalfOn, firstHalfStart, secondHalfOn, secondHalfStart):
    time = getRelativeTime(row, firstHalfOn, firstHalfStart, secondHalfOn, secondHalfStart)

    half = getHalf(firstHalfOn, secondHalfOn)

    sector = getTimeSector(time, half)

    team = getTeam(row)

    event = getEvent(row)

    player = getPlayer(row)

    location = getLocation(row)

    row = {FORMAT_ROW_TIME: time,
           FORMAT_ROW_HALF: half,
           FORMAT_ROW_SECTOR: sector,
           FORMAT_ROW_TEAM: team,
           FORMAT_ROW_EVENT: event,
           FORMAT_ROW_PLAYER: player,
           FORMAT_ROW_LOCATION: location}

    return row


def getRelativeTime(row, firstHalfOn, firstHalfStart, secondHalfOn, secondHalfStart):
    seconds = stripAndConvertTimeToInt(row['start'])

    secondsElapsed = 0

    if firstHalfOn:
        secondsElapsed = seconds - firstHalfStart
    elif secondHalfOn:
        secondsElapsed = seconds - secondHalfStart

    relativeTime = time.strftime("%M:%S", time.gmtime(secondsElapsed))

    return stripAndConvertTimeToInt(relativeTime)



def getHalf(firstHalfOn, secondHalfOn):
    if firstHalfOn is True and secondHalfOn is False:
        return 1
    elif firstHalfOn is False and secondHalfOn is True:
        return 2
    else:
        raise ValueError('Could not determine half')


def getTeam(row):
    if row['code'].startswith('opp'):
        return 'away'
    else:
        return 'home'


def getEvent(row):
    event = row['code']

    try:
        event.join(row['sourceplay'])
    except KeyError:
        pass

    return event


def getPlayer(row):
    try:
        return row['player']
    except KeyError:
        return None


def getLocation(row):
    try:
        return row['location']
    except KeyError:
        return None