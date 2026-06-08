from src.model.nba_matches import NBAMatches
from src.readers_utils.file_parser import FileParser


class NBAMatchesParser(FileParser):

    def __init__(self, file_path, file_reader):
        super().__init__(file_path, file_reader)

    def parse(self):
        return NBAMatches(self.file_reader().read(self.file_path()))
