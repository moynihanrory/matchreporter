from matchreport.collect import gaamatchcleaner
from matchreport.collect.collector import DataCollector
from matchreport.helpers import filehelper


class GaaMatchCollector(DataCollector):
    def __init__(self, inputLocation):
        super(GaaMatchCollector, self).__init__(1, inputLocation)
        self.rawData = None
        self.tidiedData = None
        self.cleanedData = None

    def tidy(self, data):
        return gaamatchcleaner.tidyData(data)

    def clean(self, data):
        return gaamatchcleaner.formatData(data)

    def read(self):
        return filehelper.readTxtFile(self.location)
