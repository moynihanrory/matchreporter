import fileHelper
import sportsCodeCleaner
from collector import DataCollector

class SportsCodeCollector(DataCollector):
    def __init__(self, inputLocation):
        super(self.__class__, self).__init__(2, inputLocation)
        self.rawData = None
        self.tidiedData = None
        self.cleanedData = None

    def tidy(self, data):
        return sportsCodeCleaner.tidyData(data)

    def clean(self, data):
        return sportsCodeCleaner.formatData(data)

    def read(self):
        return fileHelper.readXmlFile(self.location)

