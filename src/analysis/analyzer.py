from abc import abstractmethod

class Analyzer(object):
    def __init__(self, source):
        self.source = source

    @abstractmethod
    def transform(self, data):
        return NotImplemented