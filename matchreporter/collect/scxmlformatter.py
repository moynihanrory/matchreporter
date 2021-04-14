import time
from xml.etree import ElementTree as ET

from matchreporter.constants import FORMAT_ROW_TIME, \
    FORMAT_ROW_HALF, FORMAT_ROW_SECTOR, FORMAT_ROW_KPI, FORMAT_ROW_TEAM, FORMAT_ROW_LOCATION, FORMAT_ROW_PLAYER
from matchreporter.helpers.pitchgrid import Grid

from matchreporter.helpers.stringhelper import strip_and_convert_time_to_int, remove_prefix
from matchreporter.helpers.timesector import get_time_sector

XML_INSTANCE = './/instance'
VALUE_OWN = 'own '
TEAM_NAME_HOME = 'home'
TEAM_NAME_AWAY = 'away'
VALUE_OPP = 'opp '
ROW_FROM = 'from'
ROW_START = 'start'
ROW_CODE = 'code'
ROW_LOCATION = 'location'
ROW_PLAYER = 'player'
CODE = 'code'
M_S_FORMAT = "%M:%S"
FORMAT_ROW_L_ROW = 'lRow'
FORMAT_ROW_L_COLUMN = 'lColumn'
FORMAT_ROW_EVENT = 'event'
FORMAT_ROW_RAWTIME = 'rawtime'
ROW_START = 'start'
ROW_SECOND_START = '2nd start'
ROW_FIRST_START = '1st start'
ROW_TIME = 'time'
ROW_CLOCK = 'clock'
ROW_CODE = 'code'
XML_TEXT = 'text'
XML_GROUP = 'group'
OUTPUT_ROW_ID = 'id'
XML_LABEL = 'label'
XML_CODE = 'code'
XML_END = 'end'
XML_START = 'start'
XML_ID = 'ID'


def clean_and_format_data(filename):
    tree = ET.parse(filename)

    root = tree.getroot()

    flattened = flatten(root)

    rows = restructure_rows(flattened)

    return rows


def flatten(xmlroot):
    instances = xmlroot.findall(XML_INSTANCE)

    records = []

    for instance in instances:
        instance.getchildren()

        xmlid = instance.find(XML_ID)
        start = instance.find(XML_START)
        end = instance.find(XML_END)
        code = instance.find(XML_CODE)
        labels = instance.findall(XML_LABEL)

        row = {OUTPUT_ROW_ID: xmlid.text.lower(),
               XML_START: start.text.lower(),
               XML_END: end.text.lower(),
               XML_CODE: code.text.lower()
               }

        if labels is not None:
            for label in labels:
                label.getchildren()

                group = label.find(XML_GROUP)
                text = label.find(XML_TEXT)

                row.update({(group.text.lower() if group is not None else None): (text.text.lower() if text is not None else None)})

        records.append(row)

    return records


def restructure_rows(rows):
    first_half_on = False
    second_half_on = False
    is_match_on = False
    first_half_start = 0
    second_half_start = 0
    restructured_rows = []

    for index, row in enumerate(rows):
        if is_match_on is not True:
            if row[ROW_CODE] == ROW_CLOCK and row[ROW_TIME] == ROW_FIRST_START:
                first_half_start = strip_and_convert_time_to_int(row[ROW_START])
                first_half_on = True
                is_match_on = True
                continue

        if is_match_on is True:
            if row[ROW_CODE] == ROW_CLOCK and row[ROW_TIME] == ROW_SECOND_START:
                first_half_on = False
                second_half_on = True

                second_half_start = strip_and_convert_time_to_int(row[ROW_START])
                first_half_start = 0
                continue

        if is_match_on and (first_half_on or second_half_on):
            row = restructure_row(row, first_half_on, first_half_start, second_half_on, second_half_start)

            restructured_rows.append(row)

    return restructured_rows


def restructure_row(row, first_half_on, first_half_start, second_half_on, second_half_start):
    starttime, rawtime = get_relative_time(row, first_half_on, first_half_start, second_half_on, second_half_start)

    half = get_half(first_half_on, second_half_on)

    sector = get_time_sector(starttime, half)

    team = get_team(row)

    event = get_event(row)

    player = get_player(row)

    rlocation = get_reflected_location(row, half)

    l_column = None
    if rlocation is not None:
        l_column = rlocation[0:1]

    l_row = ''
    if rlocation is not None and len(rlocation) > 0:
        l_row = rlocation[-1]

    new_row = {FORMAT_ROW_TIME: starttime,
               FORMAT_ROW_RAWTIME: rawtime,
               FORMAT_ROW_HALF: half,
               FORMAT_ROW_SECTOR: sector,
               FORMAT_ROW_TEAM: team,
               FORMAT_ROW_KPI: event,
               FORMAT_ROW_EVENT: remove_prefix(remove_prefix(event, VALUE_OPP), VALUE_OWN),
               FORMAT_ROW_PLAYER: player,
               FORMAT_ROW_LOCATION: rlocation,
               FORMAT_ROW_L_COLUMN: l_column,
               FORMAT_ROW_L_ROW: l_row}

    return new_row


def get_relative_time(row, first_half_on, first_half_start, second_half_on, second_half_start):
    seconds = strip_and_convert_time_to_int(row[ROW_START])

    seconds_elapsed = 0

    if first_half_on:
        seconds_elapsed = seconds - first_half_start
    elif second_half_on:
        seconds_elapsed = seconds - second_half_start

    relative_time = time.strftime(M_S_FORMAT, time.gmtime(seconds_elapsed))

    return strip_and_convert_time_to_int(relative_time), relative_time



def get_half(first_half_on, second_half_on):
    if first_half_on is True and second_half_on is False:
        return 1

    if first_half_on is False and second_half_on is True:
        return 2

    raise ValueError('Could not determine half')


def get_team(row):
    if row[CODE].startswith(VALUE_OPP):
        return TEAM_NAME_AWAY

    return TEAM_NAME_HOME


def get_event(row):
    event = row[ROW_CODE]

    try:
        event = event + ' ' + row[ROW_FROM]
        event = event.rstrip()
    except KeyError:
        pass

    return event


def get_player(row):
    try:
        return row[ROW_PLAYER]
    except KeyError:
        return None


def get_location(row):
    try:
        return row[ROW_LOCATION]
    except KeyError:
        return None


def get_reflected_location(row, half):
    if half == 1:
        return get_location(row)
    elif half == 2:
        location = get_location(row)
        if location is not None:
            rLocation = Grid().get_reflected_pitch_sector(location)
            return rLocation
    else:
        return 'UNK'
