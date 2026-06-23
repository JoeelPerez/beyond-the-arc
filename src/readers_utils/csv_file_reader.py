import pandas as pd

from src.readers_utils.file_reader import FileReader


class CSVFileReader(FileReader):

    def read(self, file_relative_path):
        return pd.read_csv(self.get_absolute_path(file_relative_path))
