from analyzer import Analyzer
from gaaMatchCollector import GaaMatchCollector
from modes import GAAMATCH_MODE
from sportsCodeCollector import SportsCodeCollector
from transformer import Transformer

class TypeFactory(object):
    def __init__(self, args):
        self.mode = 0
        self.collector = None
        self.transformer = None
        self.analyiser = None
        self.report = None
        self.args = args

    def getCollector(self):
        if (self.collector is None and self.mode is not 0):
            self.collector = getCollectorForImportSource(self.mode, self.args)

        return self.collector

    def getTransformer(self):
        if (self.transformer is None and self.mode is not 0):
            self.transformer = getTransformerForImportSource(self.mode)

        return self.transformer

    def getAnalyzer(self):
        if (self.analyiser is None and self.mode is not 0):
            self.analyiser = getAnalyzerForImportSource(self.mode)

        return self.analyiser

    def setOperatingMode(self, mode):
        self.mode = mode
        self.collector = None
        self.transformer = None
        self.analyiser = None
        self.report = None

def getAnalyzerForImportSource(source):
    return Analyzer(source)

def getCollectorForImportSource(source, args):
    if (source == GAAMATCH_MODE):
        if args.g is None:
            return None
        return GaaMatchCollector(args.g)
    else:
        if args.x is None:
            return None
        return SportsCodeCollector(args.x)

def getTransformerForImportSource(source):
    return Transformer(source)