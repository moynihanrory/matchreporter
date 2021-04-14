from matchreporter.constants import FIRST_HALF_START, FIRST_HALF_END, SECOND_HALF_START, SECOND_HALF_END, FORMAT_ROW_TIME, \
    FORMAT_ROW_HALF, FORMAT_ROW_SECTOR, FORMAT_ROW_KPI, FORMAT_ROW_TEAM, FORMAT_ROW_LOCATION, FORMAT_ROW_PLAYER, \
    LOCATION_TAG, EVENT_ENDING
from matchreporter.helpers.pitchgrid import Grid
from matchreporter.helpers.stringhelper import strip_and_convert_half_to_int, strip_and_convert_time_to_int
from matchreporter.helpers.timesector import get_time_sector

FORMAT_ROW_ORIG_LOCATION = 'original_location'
FORMAT_ROW_L_ROW = 'lRow'
FORMAT_ROW_L_COLUMN = 'lColumn'
FORMAT_ROW_EVENT = 'event'
FORMAT_ROW_RAWTIME = 'rawtime'

def clean_and_format_data(mobile_app_output):
    first_half_on = False
    second_half_on = False
    is_match_on = False
    grid = Grid()
    formatted_lines = []

    for _, line in enumerate(mobile_app_output):
        if is_match_on is not True:
            if line.lower().startswith(FIRST_HALF_START.lower()):
                first_half_on = True
                is_match_on = True
                continue

        if is_match_on is True and first_half_on is True:
            if line.lower().startswith(FIRST_HALF_END.lower()):
                first_half_on = False
                continue

        if is_match_on is True and first_half_on is False and second_half_on is False:
            if line.lower().startswith(SECOND_HALF_START.lower()):
                second_half_on = True
                continue

        if is_match_on is True and first_half_on is False and second_half_on is True:
            if line.lower().startswith(SECOND_HALF_END.lower()):
                second_half_on = False
                is_match_on = False
                continue

        if (is_match_on and (first_half_on or second_half_on)):
            re_formatted_line = format_line(line, grid)

            formatted_lines.insert(len(formatted_lines), re_formatted_line)

    return formatted_lines


def format_line(line, grid):
    line_chunks = line.split()

    total_chunks = len(line_chunks)

    time = strip_and_convert_time_to_int(line_chunks[0])

    half = strip_and_convert_half_to_int(line_chunks[1])

    team = line_chunks[3]

    location, location_end_index = extract_location(line_chunks, total_chunks)

    pitch_location = grid.get_pitch_sector(location)

    event, event_end_index = extract_event(line_chunks, location_end_index)

    player = extract_player(line_chunks, event_end_index, location_end_index)

    sector = get_time_sector(time, half)

    l_column = None
    if pitch_location is not None and pitch_location is not 'UNK':
        l_column = pitch_location[0:1]

    l_row = ''
    if pitch_location is not None and len(pitch_location) > 0 and pitch_location is not 'UNK':
        l_row = pitch_location[-1]

    row = {FORMAT_ROW_TIME: time,
               FORMAT_ROW_RAWTIME: time,
               FORMAT_ROW_HALF: half,
               FORMAT_ROW_SECTOR: sector,
               FORMAT_ROW_TEAM: team,
               FORMAT_ROW_KPI: event,
               FORMAT_ROW_EVENT: event,
               FORMAT_ROW_PLAYER: player,
               FORMAT_ROW_LOCATION: pitch_location,
               FORMAT_ROW_L_COLUMN: l_column,
               FORMAT_ROW_L_ROW: l_row}

    return row


def extract_location(line_chunks, total_chunks):
    if LOCATION_TAG in line_chunks:
        location = line_chunks[total_chunks - 1]
    else:
        return None, total_chunks

    location_end_index = total_chunks - 1

    if location is not None:
        location_end_index = location_end_index - 1

    return location, location_end_index


def extract_event(line_chunks, event_end_index):
    player_string_start = None

    event = line_chunks[4]

    for i in range(5, event_end_index):
        event = event + ' ' + line_chunks[i]

        if line_chunks[i].lower() in EVENT_ENDING:
            player_string_start = i + 1

            break

    return event, player_string_start


def extract_player(line_chunks, player_start_index, player_end_index):
    player = ''

    if player_start_index is None or player_end_index is None:
        return player

    for i in range(player_start_index, player_end_index):
        player = player + ' ' + line_chunks[i]

    return player
