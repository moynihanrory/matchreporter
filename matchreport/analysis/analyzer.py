from matchreport.analysis.analysis import Analysis
from matchreport.constants import FORMAT_ROW_ACTION, FORMAT_ROW_TEAM, FORMAT_ROW_HALF, \
    ANA_COMMONLY_USED_TEAMS_ORDERING, FORMAT_ROW_TIME_BUCKET, FORMAT_ROW_TIME

class Analyzer(object):
    def __init__(self, source):
        self.source = source

    def analyze(self, data):
        match = data.pivot_table(index=FORMAT_ROW_ACTION,
                                 columns=FORMAT_ROW_TEAM,
                                 values=FORMAT_ROW_TIME,
                                 aggfunc='count', margins=True, fill_value=0)

        halves = data.pivot_table(index=FORMAT_ROW_ACTION,
                                  columns=[FORMAT_ROW_TEAM, FORMAT_ROW_HALF],
                                  values=FORMAT_ROW_TIME,
                                  aggfunc='count', margins=True, fill_value=0)

        sectors = data.pivot_table(index=FORMAT_ROW_ACTION,
                                   columns=[FORMAT_ROW_TEAM, FORMAT_ROW_HALF,
                                            FORMAT_ROW_TIME_BUCKET],
                                   values=FORMAT_ROW_TIME,
                                   aggfunc='count', margins=True, fill_value=0)

        return Analysis(getTeams(data), match, halves, sectors, self.source)

def getUniqueTeams(data):
    teams = data.team.unique()

    return teams

def getTeams(data):
    teams = getUniqueTeams(data)

    if teams[0].lower() not in ANA_COMMONLY_USED_TEAMS_ORDERING:
        teams[0], teams[1] = teams[1], teams[0]

    return teams

def getSectors(data):
    sectors = data.half.unique()

    return sectors


def getHalves(data):
    halves = data.sector.unique()

    return halves