import pandas as pd
from sklearn.preprocessing import StandardScaler


class DataNormalizer:

    def __init__(self):
        self.__normalizer = StandardScaler()

    def normalize(self, data):
        return pd.DataFrame(self.__normalizer.fit_transform(data), columns=list(data))
