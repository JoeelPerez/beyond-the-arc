import unittest

from src.config.config import START_2026_REGULAR_SEASON, END_2026_REGULAR_SEASON
from src.readers_utils.csv_file_reader import CSVFileReader
from src.readers_utils.nba_matches_parser import NBAMatchesParser


class NBAMatchesTest(unittest.TestCase):
    file_path = "data/TeamStatistics.csv"
    example_team_name = "Cavaliers"
    selected_columns = ["teamCity", "teamName", "teamId"]
    deleted_columns = ["opponentTeamName", "opponentTeamId", "home"]

    def test_nba_matches_team_name_filter(self):
        nba_matches = NBAMatchesParser(self.file_path, CSVFileReader()).parse()
        nba_matches_dataframe = nba_matches.filter_team_name(self.example_team_name).get_matches()
        assert nba_matches_dataframe["teamName"].values[0] == self.example_team_name

    def test_nba_matches_date_filter(self):
        nba_matches = NBAMatchesParser(self.file_path, CSVFileReader()).parse()
        nba_matches_dataframe = nba_matches.filter_date(START_2026_REGULAR_SEASON, END_2026_REGULAR_SEASON) \
            .get_matches()
        assert nba_matches_dataframe["gameDate"].between(START_2026_REGULAR_SEASON, END_2026_REGULAR_SEASON).all()

    def test_nba_matches_select_columns(self):
        nba_matches = NBAMatchesParser(self.file_path, CSVFileReader()).parse()
        nba_matches_dataframe = nba_matches.select_columns(self.selected_columns).get_matches()
        assert nba_matches_dataframe.columns.isin(self.selected_columns).all()
        assert not nba_matches_dataframe.columns.isin(self.deleted_columns).any()

    def test_nba_matches_delete_columns(self):
        nba_matches = NBAMatchesParser(self.file_path, CSVFileReader()).parse()
        nba_matches_dataframe = nba_matches.delete_columns(self.deleted_columns).get_matches()
        assert nba_matches_dataframe.columns.isin(self.selected_columns).any()
        assert not nba_matches_dataframe.columns.isin(self.deleted_columns).any()


if __name__ == '__main__':
    unittest.main()
