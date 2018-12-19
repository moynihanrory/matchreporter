import gaaMatchCleaner
import fileHelper
from collector import DataCollector

class GaaMatchCollector(DataCollector):
    def __init__(self, inputLocation):
        super(self.__class__, self).__init__(1, inputLocation)
        self.rawData = None
        self.tidiedData = None
        self.cleanedData = None

    def tidy(self, data):
        return gaaMatchCleaner.tidyData(data)

    def clean(self, data):
        return gaaMatchCleaner.formatData(data)

    def read(self):
        return fileHelper.readTxtFile(self.location)
