
# Constants
# Mongo
MDB_DATABASE_NAME = 'analysis'
MDB_PASSWORD = 'liv01p01l'
MDB_USERNAME = 'rory'
MDB_IMPORT_FILE___TXT = 'import_file_{}.txt'
MDB_IMPORT_FILE_SOURCE_TXT = 'TEXT'
MDB_DATETIME_FORMAT = '%Y-%m-%d-%H-%M-%S'
MDB_DATE_FORMAT = '%Y-%m-%d'
MDB_MLAB_URL = "mongodb://ds119374.mlab.com:19374"
MDB_ORIGINAL_DOC_NAME = 'gaaMatchImportData'
MDB_CLEANED_DOC_NAME = 'gaaMatchCleanedData'
MDB_CLEANED_DATA_CONTENTS_COLUMN_NAME = 'contents'
MDB_SPORTSCODE_DOC_NAME = 'sportsCodeImportData'
MDB_TRANSFORMED_DATA_NAME = 'transformedData'
MDB_TRANSFORM_MAPPING_NAME = 'mappingData'
MDB_TRANSFORM_TABLENAME_TEMPLATE = 'transformedData_{}'

# SQL Database constants
DB_FILENAME = 'GAAMatch.sqlite'
DB_TABLENAME = 'zstats'
DB_C1 = 'zstats1'
DB_C2 = 'zstats2'
DB_C3 = 'ztype'
DB_C4 = 'zperiod'
DB_C5 = 'zplayer'
DB_C6 = 'zteam'
DB_C7 = 'ztimegone'
DB_PREPARED_QUERY = 'SELECT {c1},{c2},{c3},{c4},{c5},{c6},{c7} FROM {t}'.\
    format(c1=DB_C1,c2=DB_C2,c3=DB_C3,c4=DB_C4,c5=DB_C5,c6=DB_C6,c7=DB_C7,t=DB_TABLENAME)

# File constants
FILE_NAME = 'stats.txt'
FILE_REL_OUTPUT_DIRECTORY = './match/'

# Data Tidy constants
TIDY_EMPTY = ''
TIDY_SI = 5
TIDY_LS1 = 'GAA'
TIDY_LS2 = 'Half'
TIDY_LS3 = 'Team'
TIDY_LS4 = 'Match'
TIDY_LS5 = 'MATCH'
TIDY_LS6 = 'Full'
TIDY_LS7 = '1st'
TIDY_LS8 = '2nd'
TIDY_LS9 = 'Sent'
TIDY_LS10 = '2'
TIDY_SKIP = True
TIDY_PROCESS = False
TIDY_EVENT_FROM = ['play', 'free', 'penalty', '45/65', 'sideline', 'card', 'won', 'lost', 'conceded']
TIDY_STR_MINS = 'mins'
TIDY_FULL_TIME = 'Full time'

FORMAT_ROW_PLAYER = 'player'
FORMAT_ROW_ACTION = 'kpi'
FORMAT_ROW_TEAM = 'team'
FORMAT_ROW_HALF = 'half'
FORMAT_ROW_TIME_BUCKET = 'sector'
FORMAT_ROW_TIME = 'time'

# Helper constants
TIME_HELPER_STR_ZERO = '0'
TIME_HELPER_STR_COLON = ':'
TIME_HELPER_INT_ZERO = 0
TIME_HELPER_INT_ONE = 1
TIME_HELPER_INT_TWO = 2
TIME_HELPER_INT_SECTOR_PER_HALF = 3
TIME_HELPER_INT_SECTOR_LAST_POS = 5

# Data Transform constants
TX_KPI_COLUMN_NAME = 'kpi'

# Analyzer
ANA_COMMONLY_USED_TEAMS_ORDERING = ['maroon', 'craughwell', 'galway']
ANA_GROUPBY_COLUMN_NAMES_MATCH = [FORMAT_ROW_TEAM, FORMAT_ROW_ACTION]
ANA_GROUPBY_COLUMN_NAMES_HALF = [FORMAT_ROW_TEAM, FORMAT_ROW_HALF, FORMAT_ROW_ACTION]
ANA_GROUPBY_COLUMN_NAMES_SECTOR = [FORMAT_ROW_TEAM, FORMAT_ROW_HALF, FORMAT_ROW_TIME_BUCKET, FORMAT_ROW_ACTION]

# Excel
EX_OUTPUT_REPORT_FILE = 'report_{}_{}_{}.xlsx'
EX_SECTORS_SHEET_NAME = 'Sectors'
EX_HALVES_SHEET_NAME = 'Halves'
EX_MATCH_SHEET_NAME = 'Match'
EX_KPI_SHEET_NAME = 'KPIs'