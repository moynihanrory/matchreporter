from abc import abstractmethod

from analysis import Analysis
from analyzer import Analyzer
from constants import FORMAT_ROW_ACTION, FORMAT_ROW_TEAM, FORMAT_ROW_HALF, ANA_COMMONLY_USED_TEAMS_ORDERING, \
    FORMAT_ROW_TIME_BUCKET, FORMAT_ROW_TIME


class GaaMatchAnalyzer(Analyzer):
    def __init__(self, source):
        self.source = source

    @abstractmethod
    def analyze(self, data):
        # get the list of items to group
        match = data.pivot_table(index=FORMAT_ROW_ACTION, columns=FORMAT_ROW_TEAM, values=FORMAT_ROW_TIME,
                                 aggfunc='count', margins=True, fill_value=0)

        halves = data.pivot_table(index=FORMAT_ROW_ACTION, columns=[FORMAT_ROW_TEAM, FORMAT_ROW_HALF], values=FORMAT_ROW_TIME,
                                 aggfunc='count', margins=True, fill_value=0)

        sectors = data.pivot_table(index=FORMAT_ROW_ACTION, columns=[FORMAT_ROW_TEAM, FORMAT_ROW_HALF, FORMAT_ROW_TIME_BUCKET], values=FORMAT_ROW_TIME,
                                 aggfunc='count', margins=True, fill_value=0)

        return Analysis(self._getTeams(data), match, halves, sectors)

    def _getUniqueTeams(self, data):
        teams = data.team.unique()

        return teams

    def _getTeams(self, data):
        teams = self._getUniqueTeams(data)

        if (teams[0].lower() not in ANA_COMMONLY_USED_TEAMS_ORDERING):
            teams[0], teams[1] = teams[1], teams[0]

        return teams

    def _getSectors(self, data):
        sectors = data.half.unique()

        return sectors

    def _getHalves(self, data):
        halves = data.sector.unique()

        return halves

