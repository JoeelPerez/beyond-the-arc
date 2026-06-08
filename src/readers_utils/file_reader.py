from abc import ABC, abstractmethod

from src.config.config import BASE_DIR


class FileReader(ABC):

    @abstractmethod
    def read(self, file_path):
        pass

    def get_absolute_path(self, relative_file_path):
        return f"{BASE_DIR}/{relative_file_path}"
