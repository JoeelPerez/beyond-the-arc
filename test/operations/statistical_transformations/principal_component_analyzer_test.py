import unittest

from src.readers_utils.csv_file_reader import CSVFileReader
from src.readers_utils.nba_matches_parser import NBAMatchesParser
from src.operations.statistical_transformations.data_normalizer import DataNormalizer
from src.operations.statistical_transformations.principal_component_analyzer import PrincipalComponentAnalyzer


class PrincipalComponentAnalysisTest(unittest.TestCase):
    file_path = "data/TeamStatistics.csv"
    selected_columns = ["teamName", "teamScore", "opponentScore", "assists", "blocks"]

    def __get_dataframe(self, columns):
        nba_matches = NBAMatchesParser(self.file_path, CSVFileReader()).parse()
        nba_matches_dataframe = nba_matches.select_columns(columns) \
            .apply_aggregation_by_column(["teamName"], "mean") \
            .get_matches()
        return nba_matches_dataframe[~nba_matches_dataframe.isna().any(axis=1)]

    def test_principal_component_analyzer_without_index(self):
        dataframe = self.__get_dataframe(self.selected_columns)
        pca_dataframe = PrincipalComponentAnalyzer(DataNormalizer(), 2).execute_analysis(dataframe)
        print(pca_dataframe)

    def test_principal_component_analyzer_with_index(self):
        dataframe = self.__get_dataframe(self.selected_columns)
        pca_dataframe = PrincipalComponentAnalyzer(DataNormalizer(), 2).execute_analysis(dataframe, True)
        print(pca_dataframe)


if __name__ == '__main__':
    unittest.main()