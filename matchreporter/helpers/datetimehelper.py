from datetime import datetime
from matchreporter.constants import DATE_FORMAT


def get_todays_date():
    return datetime.strftime(datetime.now(), DATE_FORMAT)
