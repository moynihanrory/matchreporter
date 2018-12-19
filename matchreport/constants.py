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
#sportscode
TIDY_SCX_CODE = 'code'
TIDY_SCX_OBS_1 = 'file'
TIDY_SCX_OBS_2 = 'ALL_INSTANCES'
TIDY_SCX_OBS_3 = 'instance'
TIDY_SCX_START = 'start'
TIDY_SCX_END = 'end'
TIDY_SCX_UNDERSCORE = '_'
TIDY_SCX_OBS_TEAM_1 = 'GAL'
TIDY_SCX_OBS_TEAM_2 = 'OPP'
TIDY_SCX_OBS_HT = 'HT'

FORMAT_ROW_PLAYER = 'player'
FORMAT_ROW_ACTION = 'kpi'
FORMAT_ROW_TEAM = 'team'
FORMAT_ROW_HALF = 'half'
FORMAT_ROW_TIME_BUCKET = 'sector'
FORMAT_ROW_TIME = 'time'

MDB_IMPORT_FILE_TXT = 'import_file_{}.txt'
MDB_IMPORT_FILE_SOURCE_TXT = 'TEXT'
MDB_DATETIME_FORMAT = '%Y-%m-%d-%H-%M-%S'
MDB_DATE_FORMAT = '%Y-%m-%d'

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
EX_OUTPUT_REPORT_FILE_SHEET = '{}_{}'
