import pandas as pd
from sklearn.decomposition import PCA


class PrincipalComponentAnalyzer:

    def __init__(self, data_normalizer, components_number):
        self.__data_normalizer = data_normalizer
        self.__pca_analyzer = PCA(n_components=components_number)
        self.__columns_name = self.__get_columns_names(components_number)

    def __get_columns_names(self, components_number):
        return [f"PCA_{i + 1}" for i in range(components_number)]

    def __get_row_index(self, data):
        column_values = list(data.index)
        return {i: column_values[i] for i in range(len(column_values))}

    def execute_analysis(self, data, add_index=False):
        normalized_data = self.__data_normalizer.normalize(data)
        pca_dataframe = pd.DataFrame(self.__pca_analyzer.fit_transform(normalized_data), columns=self.__columns_name)
        if not add_index:
            return pca_dataframe
        return pca_dataframe.rename(index=self.__get_row_index(data))
