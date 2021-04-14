import time
from matchreporter.db.database import create_record, create_records

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
INSERT_MATCH_SQL = "INSERT INTO `analysis`.`match`(`team1`,`team2`,`date`,`source`)VALUES(%s,%s,%s,%s); "
MATCH_EVENTS_TABLENAME = "match_events"
MATCH_PLAYS_TABLENAME = "match_plays"
EVENTS_COL_NAME = 'events'
MATCH_ID_COL_NAME = 'match_id'


def write_report_data(source, analysis):
    newid = create_match(source, analysis)

    print("New report entered with id:", newid)

    create_match_events(analysis, newid)

    return create_match_plays(analysis, newid)


def create_match(source, analysis):
    teams = analysis.teams
    args = (teams[0], teams[1], time.strftime(TIME_FORMAT), source)

    newid = create_record(INSERT_MATCH_SQL, args)

    return newid


def create_match_events(analysis, rowid):
    match_events = analysis.raw

    match_events[MATCH_ID_COL_NAME] = rowid

    return create_records(MATCH_EVENTS_TABLENAME, match_events)


def create_match_plays(analysis, rowid):
    match_plays = analysis.plays

    match_plays[MATCH_ID_COL_NAME] = rowid

    match_plays[EVENTS_COL_NAME] = match_plays[EVENTS_COL_NAME].astype(str)

    return create_records(MATCH_PLAYS_TABLENAME, match_plays)
