
class Analysis(object):
    def __init__(self, raw, teams, matchBreakdown, players1Breakdown, players2Breakdown, halvesBreakdown, sectorsBreakdown,
                 sectors1, sectors2, location1Breakdown, location2Breakdown, possessions, tackles):

        self.raw = raw
        self.teams = teams
        self.match = matchBreakdown
        self.players1 = players1Breakdown
        self.players2 = players2Breakdown
        self.halves = halvesBreakdown
        self.sectors = sectorsBreakdown
        self.sectors1 = sectors1
        self.sectors2 = sectors2
        self.location1 = location1Breakdown
        self.location2 = location2Breakdown
        self.possessions = possessions
        self.tackles = tackles

