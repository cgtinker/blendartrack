from abc import ABC, abstractmethod


class ImportModel(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def prepare(self, model, batch):
        pass

    @abstractmethod
    def execute(self):
        pass
