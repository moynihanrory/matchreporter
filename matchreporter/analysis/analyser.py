import pandas as pd

from matchreporter.analysis.play_anayliser import analyise_plays


class Analysis:
    def __init__(self, raw, teams, plays):

        self.raw = raw
        self.teams = teams
        self.plays = plays


def analyse(data):
    data_frame = pd.DataFrame(data)

    teams = get_teams(data_frame)

    plays = analyise_plays(data)

    return Analysis(data_frame, teams, plays)


def get_unique_teams(data):
    teams = data.team.unique()

    return teams


def get_teams(data):
    teams = get_unique_teams(data)

    return teams


