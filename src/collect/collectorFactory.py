from gaaMatchCollector import GaaMatchCollector

def getCollectorForImportSource(source):
    if (source == 1):
        collector = GaaMatchCollector()
        return collector
    else:
        return None
