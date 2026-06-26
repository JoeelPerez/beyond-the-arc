import pandas as pd
from sklearn.preprocessing import StandardScaler


class DataNormalizer:

    def __init__(self):
        self.__normalizer = StandardScaler()

    def normalize(self, dataframe, keep_row_index=False):
        if keep_row_index:
            return pd.DataFrame(self.__normalizer.fit_transform(dataframe),
                                columns=list(dataframe),
                                index=list(dataframe.index))
        return pd.DataFrame(self.__normalizer.fit_transform(dataframe), columns=list(dataframe))
