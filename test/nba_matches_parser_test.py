import unittest

from src.model.nba_matches import NBAMatches
from src.readers_utils.CSVFileReader import CSVFileReader
from src.readers_utils.nba_matches_parser import NBAMatchesParser


class NBAMatchesParserTest(unittest.TestCase):
    file_path = "data/TeamStatistics.csv"

    def test_nba_matches_parser(self):
        nba_matches = NBAMatchesParser(self.file_path, CSVFileReader()).parse()
        self.assertIsInstance(nba_matches, NBAMatches)


if __name__ == '__main__':
    unittest.main()
