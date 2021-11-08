from abc import ABC, abstractmethod


class CustomData(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def execute(self):
        pass
