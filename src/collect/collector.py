from abc import abstractmethod

class DataCollector(object):
    def __init__(self, source, inputLocation):
        self.source = source
        self.location = inputLocation
        self.rawData = None
        self.cleanedData = None
        self.tidiedData = None

    @abstractmethod
    def read(self):
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

    @abstractmethod
    def cleanAndImportData(self):

        try:
            if (self.rawData is None):
                self.rawData = self.read()
        except FileNotFoundError:
            return None

        self.tidiedData = self.tidy(self.rawData)

        self.cleanedData = self.clean(self.tidiedData)

        return self.cleanedData

    @abstractmethod
    def getImportData(self):
        return self.rawData
