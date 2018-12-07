import mongoManager
from constants import TX_KPI_COLUMN_NAME
from transformer import Transformer
from gaaMatchEventsMap import createEventLookupTable
import pandas as pd


class GaaMatchTransformer(Transformer):

    def __init__(self):
        super(self.__class__, self).__init__(1)
        self.mapping = None
        self.transformedData = None

    def transform(self, data):
        if (data is None):
            return

        if (self.mapping is None):
            self.mapping = createEventLookupTable()

        transformedDataFrame = pd.DataFrame(data)

        transformedDataFrame[TX_KPI_COLUMN_NAME] = transformedDataFrame[TX_KPI_COLUMN_NAME].replace(self.mapping)

        self.transformedData = transformedDataFrame

        return self.transformedData

    def getTransformedDataById(self, transformedDataOid):
        if (self.transformedData is not None):
            return self.transformedData

        self.transformedData = mongoManager.getTransformedDataById(transformedDataOid)