import unittest

from src.readers_utils.csv_file_reader import CSVFileReader
from src.readers_utils.nba_matches_parser import NBAMatchesParser


class NBAMatchesTest(unittest.TestCase):
    file_path = "data/TeamStatistics.csv"
    example_team_name = "Cavaliers"

    def test_nba_matches_team_name_filter(self):
        nba_matches = NBAMatchesParser(self.file_path, CSVFileReader()).parse()
        nba_matches_dataframe = nba_matches.filter_team_name(self.example_team_name).get_matches()
        assert(nba_matches_dataframe["teamName"].values[0] == self.example_team_name)


if __name__ == '__main__':
    unittest.main()
