import math
import unittest

from src.readers_utils.csv_file_reader import CSVFileReader
from src.operations.statistical_transformations.data_normalizer import DataNormalizer


class DataNormalizerTest(unittest.TestCase):
    file_path = "data/TeamStatistics.csv"
    selected_columns = ["teamScore", "opponentScore", "assists", "reboundsTotal"]

    def test_data_normalizer(self):
        dataframe = CSVFileReader().read(self.file_path)[self.selected_columns]
        normalized_dataframe = DataNormalizer().normalize(dataframe)
        assert math.isclose(0, normalized_dataframe["assists"].mean(), abs_tol=1e-9)
        assert math.isclose(1, normalized_dataframe["opponentScore"].std(), abs_tol=1e-5)


if __name__ == '__main__':
    unittest.main()
