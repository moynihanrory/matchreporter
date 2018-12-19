
from matchreport.collect import sportscodecleaner
from matchreport.collect.collector import DataCollector
from matchreport.helpers import filehelper

class SportsCodeCollector(DataCollector):
    def __init__(self, inputLocation):
        super(SportsCodeCollector, self).__init__(2, inputLocation)
        self.rawData = None
        self.tidiedData = None
        self.cleanedData = None

    def tidy(self, data):
        return sportscodecleaner.tidyData(data)

    def clean(self, data):
        return sportscodecleaner.formatData(data)

    def read(self):
        return filehelper.readXmlFile(self.location)

