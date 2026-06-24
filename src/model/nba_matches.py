import pandas as pd


class NBAMatches:
    TEAM_COLUMN_NAME = "teamName"
    MATCH_DATE_COLUMN_NAME = "gameDate"

    def __init__(self, nba_matches_dataset):
        self.__nba_matches_dataset = nba_matches_dataset
        self.__cast_column_to_date(self.MATCH_DATE_COLUMN_NAME)

    def __cast_column_to_date(self, column_name):
        self.__nba_matches_dataset[column_name] = pd.to_datetime(self.__nba_matches_dataset[column_name])

    def get_matches(self):
        return self.__nba_matches_dataset

    def filter_team_name(self, team_name):
        self.__nba_matches_dataset = self.__nba_matches_dataset[
            self.__nba_matches_dataset[self.TEAM_COLUMN_NAME] == team_name]
        return self

    def filter_date(self, start_date, end_date):
        self.__nba_matches_dataset = self.__nba_matches_dataset[
            self.__nba_matches_dataset[self.MATCH_DATE_COLUMN_NAME].between(start_date, end_date)]
        return self
