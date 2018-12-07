from gaaMatchAnalyiser import GaaMatchAnalyzer

def getAnalyzerForImportSource(source):
    if (source == 1):
        analyzer = GaaMatchAnalyzer(source)
        return analyzer
    else:
        return None
