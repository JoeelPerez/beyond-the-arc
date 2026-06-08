from abc import ABC, abstractmethod


class FileParser(ABC):

    def __init__(self, file_path, file_reader):
        self.__file_path = file_path
        self.__file_reader = file_reader

    @abstractmethod
    def parse(self):
        pass

    def file_path(self):
        return self.__file_path

    def file_reader(self):
        return self.__file_reader
