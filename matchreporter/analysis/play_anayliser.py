import pandas as pd

from matchreporter.analysis.events import is_origin_of_play_event, is_outcome_of_play_event, \
    is_transition_play_event, is_middle_play_event, transpose_outcome
from matchreporter.analysis.play import get_play

CLOCK = 'clock'
PLAYID = 'playid'
KPI = 'kpi'
REDUCED_ORIGIN = 'reduced_origin'
REDUCED_OUTCOME = 'reduced_outcome'


def analyise_plays(row_list):
    play_list = create_playlist(row_list)

    data_frame = convert_playlist_to_dataframe(play_list)

    data_frame = transform_dataframe(data_frame)

    return data_frame


def transform_dataframe(data_frame):
    data_frame = transform_outcomes(data_frame)
    data_frame = transform_origins(data_frame)
    return data_frame


def transform_outcomes(dataframe):
    dataframe[REDUCED_OUTCOME] = dataframe.outcome.apply(lambda row: transpose_outcome(row))

    return dataframe


def transform_origins(dataframe):
    dataframe[REDUCED_ORIGIN] = dataframe.origin.apply(lambda row: transpose_outcome(row))

    return dataframe


def convert_playlist_to_dataframe(play_list):
    data_frame = pd.DataFrame([p.__dict__ for p in play_list])

    return data_frame


def create_playlist(row_list):
    listofplays = []

    play = get_play()

    for _, row in enumerate(row_list):

        if is_origin_of_play_event(row):
            play = set_origin(play, row)

        elif is_outcome_of_play_event(row):
            set_outcome(listofplays, play, row)

        elif is_transition_play_event(row):
            set_outcome(listofplays, play, row)
            play = set_origin(play, row)

        elif is_middle_play_event(row):
            play.add_event(row)
        else:
            if row[KPI] != CLOCK:
                print("ERROR: Unknown event: ", row[KPI],  " : ", row)

        play_dict = {PLAYID: play.playid}
        row.update(play_dict)

    return listofplays


def set_origin(play, row):
    play = get_play()
    play.add_origin_event(row)
    return play


def set_outcome(listofplays, play, row):
    play.add_outcome_event(row)
    listofplays.append(play)
