TEAM_NAME_COLUMN = "teamName"


class NBAMatches:

    def __init__(self, nba_matches_dataset):
        self.__nba_matches_dataset = nba_matches_dataset

    def get_matches(self):
        return self.__nba_matches_dataset

    def filter_team_name(self, team_name):
        self.__nba_matches_dataset = self.__nba_matches_dataset[
            self.__nba_matches_dataset[TEAM_NAME_COLUMN] == team_name]
        return self
