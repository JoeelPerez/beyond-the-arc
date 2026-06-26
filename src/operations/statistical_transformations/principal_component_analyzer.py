import pandas as pd
from sklearn.decomposition import PCA


class PrincipalComponentAnalyzer:

    def __init__(self, data_normalizer, components_number):
        self.__data_normalizer = data_normalizer
        self.__pca_analyzer = PCA(n_components=components_number)
        self.__columns_name = self.__get_columns_names(components_number)

    def __get_columns_names(self, components_number):
        return [f"PCA_{i + 1}" for i in range(components_number)]

    def __get_row_index(self, dataframe):
        column_values = list(dataframe.index)
        return {i: column_values[i] for i in range(len(column_values))}

    def __execute_pca(self, dataframe, row_index=None):
        return pd.DataFrame(self.__pca_analyzer.fit_transform(dataframe),
                            columns=self.__columns_name,
                            index=row_index)

    def execute_analysis(self, dataframe, keep_row_index=False):
        normalized_data = self.__data_normalizer.normalize(dataframe, keep_row_index)
        if keep_row_index:
            return self.__execute_pca(normalized_data, list(normalized_data.index))
        return self.__execute_pca(normalized_data)
