from abc import abstractmethod

class DataCollector(object):

    def __init__(self, source):
        self.source = source

    @abstractmethod
    def read(self, source):
        return NotImplemented

    @abstractmethod
    def tidy(self, data):
        return NotImplemented

    @abstractmethod
    def clean(self, data):
        return NotImplemented

    @abstractmethod
    def cleanAndImportData(self, data):
        return NotImplemented