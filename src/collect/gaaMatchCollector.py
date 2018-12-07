import cleaner
import fileHelper
import mongoManager
from collector import DataCollector


class GaaMatchCollector(DataCollector):

    def __init__(self):
        super(self.__class__, self).__init__(1)
        self.rawData = None
        self.tidiedData = None
        self.cleanedData = None

    def read(self, source):
        return self._readGaaMatchExportFile(source)

    def tidy(self, data):
        return cleaner.tidyData(data)

    def clean(self, data):
        return cleaner.formatData(data)

    def _readGaaMatchExportFile(self, oid):
        return fileHelper.readTxtFile(oid)

    def cleanAndImportData(self, filename):

        try:
            if (self.rawData is None):
                self.rawData = self.read(filename)
        except FileNotFoundError:
            return None

        self.tidiedData = self.tidy(self.rawData)

        self.cleanedData = self.clean(self.tidiedData)

        return self.cleanedData

    def getImportData(self):
        return self.rawData

    def getCleanedDataById(self, cleanedDataOid):
        if (self.cleanedData is not None):
            return self.cleanedData

        self.cleanedData = mongoManager.getCleanedDataByOriginalId(cleanedDataOid)