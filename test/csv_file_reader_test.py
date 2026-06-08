import unittest
import os

from src.readers_utils.CSVFileReader import CSVFileReader


class CSVFileReaderTest(unittest.TestCase):
    file_path = "data/TeamStatistics.csv"

    def test_read_file(self):
        print(CSVFileReader().read(self.file_path))


if __name__ == '__main__':
    unittest.main()
