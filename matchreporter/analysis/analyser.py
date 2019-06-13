import pandas as pd

from matchreporter.analysis.analysis import Analysis
from matchreporter.constants import FORMAT_ROW_EVENT, FORMAT_ROW_TEAM, FORMAT_ROW_TIME, FORMAT_ROW_HALF, \
    FORMAT_ROW_SECTOR, TEAM_COLUMN, FORMAT_ROW_LOCATION, FORMAT_ROW_PLAYER



def analyse(data):
    df = pd.DataFrame(data)

    match = df.pivot_table(index=FORMAT_ROW_EVENT,
                           columns=FORMAT_ROW_TEAM,
                           values=FORMAT_ROW_TIME,
                           aggfunc='count', margins=True, fill_value=0)

    halves = df.pivot_table(index=FORMAT_ROW_EVENT,
                            columns=[FORMAT_ROW_TEAM, FORMAT_ROW_HALF],
                            values=FORMAT_ROW_TIME,
                            aggfunc='count', margins=True, fill_value=0)

    sectors = df.pivot_table(index=FORMAT_ROW_EVENT,
                             columns=[FORMAT_ROW_TEAM, FORMAT_ROW_HALF, FORMAT_ROW_SECTOR],
                             values=FORMAT_ROW_TIME,
                             aggfunc='count', margins=True, fill_value=0)

    team1 = df.loc[df[TEAM_COLUMN] == getUniqueTeams(df)[0]]
    team2 = df.loc[df[TEAM_COLUMN] == getUniqueTeams(df)[1]]

    location1 = None
    location2 = None

    if (countLocations(df) > 2):
        location1 = team1.pivot_table(index=FORMAT_ROW_EVENT,
                               columns=[FORMAT_ROW_TEAM, FORMAT_ROW_LOCATION],
                               values=FORMAT_ROW_TIME,
                               aggfunc='count', margins=True, fill_value=0)

        location2 = team2.pivot_table(index=FORMAT_ROW_EVENT,
                               columns=[FORMAT_ROW_TEAM, FORMAT_ROW_LOCATION],
                               values=FORMAT_ROW_TIME,
                               aggfunc='count', margins=True, fill_value=0)

    players1 = team1.pivot_table(index=FORMAT_ROW_EVENT,
                           columns=FORMAT_ROW_PLAYER,
                           values=FORMAT_ROW_TIME,
                           aggfunc='count', margins=True, fill_value=0)

    players2 = team2.pivot_table(index=FORMAT_ROW_EVENT,
                           columns=FORMAT_ROW_PLAYER,
                           values=FORMAT_ROW_TIME,
                           aggfunc='count', margins=True, fill_value=0)

    sectors1 = team1.pivot_table(index=FORMAT_ROW_EVENT,
                             columns=[FORMAT_ROW_TEAM, FORMAT_ROW_HALF, FORMAT_ROW_SECTOR],
                             values=FORMAT_ROW_TIME,
                             aggfunc='count', margins=True, fill_value=0)

    sectors2 = team2.pivot_table(index=FORMAT_ROW_EVENT,
                             columns=[FORMAT_ROW_TEAM, FORMAT_ROW_HALF, FORMAT_ROW_SECTOR],
                             values=FORMAT_ROW_TIME,
                             aggfunc='count', margins=True, fill_value=0)

    possessionData = df.loc[df[FORMAT_ROW_EVENT] == 'possession']
    tackleData = df.loc[df[FORMAT_ROW_EVENT] == 'tackle']

    possessions = None
    if possessionData is not None and not possessionData.empty:
        possessions = possessionData.pivot_table(index=FORMAT_ROW_PLAYER,
                                 columns=[FORMAT_ROW_TEAM],
                                 values=FORMAT_ROW_TIME,
                                 aggfunc='count', margins=True, fill_value=0)

    tackles = None
    if tackleData is not None and not tackleData.empty:
        tackles = tackleData.pivot_table(index=FORMAT_ROW_PLAYER,
                                 columns=[FORMAT_ROW_TEAM],
                                 values=FORMAT_ROW_TIME,
                                 aggfunc='count', margins=True, fill_value=0)

    return Analysis(df,
                    getTeams(df),
                    match,
                    players1,
                    players2,
                    halves,
                    sectors,
                    sectors1,
                    sectors2,
                    location1,
                    location2,
                    possessions,
                    tackles)


def getUniqueTeams(data):
    teams = data.team.unique()

    if (teams[0] in (['Craughwell', 'Galway'])) == False:
        teams.sort(axis=0)

    return teams


def getTeams(data):
    teams = getUniqueTeams(data)

    return teams


def getSectors(data):
    sectors = data.half.unique()

    return sectors


def getHalves(data):
    halves = data.sector.unique()

    return halves


def countLocations(data):
    locations = data.location.unique()

    return len(locations)