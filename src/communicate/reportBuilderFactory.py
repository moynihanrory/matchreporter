
from matchReport import Report


def getReportBuilderForImportSource(source):
    if (source == 1):
        reportBuilder = Report(source)
        return reportBuilder
    else:
        return None
