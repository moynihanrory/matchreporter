import pandas as pd
from constants import TX_KPI_COLUMN_NAME

class Transformer(object):
    def __init__(self, source):
        self.source = source

    def transform(self, data):
        if (data is None):
            return

        transformedDataFrame = pd.DataFrame(data)

        transformedDataFrame[TX_KPI_COLUMN_NAME] = transformedDataFrame[TX_KPI_COLUMN_NAME]

        self.transformedData = transformedDataFrame

        return self.transformedData
