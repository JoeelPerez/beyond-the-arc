from src.config.config import START_2026_REGULAR_SEASON, END_2026_REGULAR_SEASON, ALL_STARS_TEAMS
from src.readers_utils.csv_file_reader import CSVFileReader
from src.readers_utils.nba_matches_parser import NBAMatchesParser

if __name__ == "__main__":

    file_path = "data/TeamStatistics.csv"
    selected_columns = ["teamScore", "opponentScore", "assists", "reboundsTotal", "teamName"]

    nba_matches = NBAMatchesParser(file_path, CSVFileReader()).parse()
    nba_matches_dataframe = nba_matches.filter_date(START_2026_REGULAR_SEASON, END_2026_REGULAR_SEASON) \
        .filter_without_team_name(ALL_STARS_TEAMS) \
        .select_columns(selected_columns) \
        .apply_aggregation_by_column(["teamName"], "mean") \
        .get_matches()
    print(nba_matches_dataframe)
