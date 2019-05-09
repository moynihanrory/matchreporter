from datetime import datetime
from matchreporter.constants import DATE_FORMAT


def getTodaysDate():
    return datetime.strftime(datetime.now(), DATE_FORMAT)