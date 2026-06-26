import math
import unittest

from src.readers_utils.csv_file_reader import CSVFileReader
from src.operations.statistical_transformations.data_normalizer import DataNormalizer
from src.readers_utils.nba_matches_parser import NBAMatchesParser


class DataNormalizerTest(unittest.TestCase):
    file_path = "data/TeamStatistics.csv"
    selected_columns = ["teamName", "teamScore", "opponentScore", "assists", "reboundsTotal"]

    def __get_dataframe(self, columns):
        nba_matches = NBAMatchesParser(self.file_path, CSVFileReader()).parse()
        nba_matches_dataframe = nba_matches.select_columns(columns) \
            .apply_aggregation_by_column(["teamName"], "mean") \
            .get_matches()
        return nba_matches_dataframe[~nba_matches_dataframe.isna().any(axis=1)]

    def test_data_normalizer_without_row_index(self):
        dataframe = self.__get_dataframe(self.selected_columns)
        normalized_dataframe = DataNormalizer().normalize(dataframe)
        assert math.isclose(0, normalized_dataframe["assists"].mean(), abs_tol=1e-9)
        assert math.isclose(1, normalized_dataframe["opponentScore"].std(), abs_tol=0.1)

    def test_data_normalizer_with_row_index(self):
        dataframe = self.__get_dataframe(self.selected_columns)
        normalized_dataframe = DataNormalizer().normalize(dataframe, True)
        assert math.isclose(0, normalized_dataframe["assists"].mean(), abs_tol=1e-9)
        assert math.isclose(1, normalized_dataframe["reboundsTotal"].std(), abs_tol=0.1)


if __name__ == '__main__':
    unittest.main()
