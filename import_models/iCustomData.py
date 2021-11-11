from abc import ABC, abstractmethod


class ImportModel(ABC):
    @abstractmethod
    def __init__(self, json_data, title, batch):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def animate(self):
        pass

    @abstractmethod
    def structure(self):
        pass
