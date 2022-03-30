from abc import ABC, abstractmethod


class ImportModel(ABC):
    @abstractmethod
    def initialize(self):
        """ initialize the data by creating custom data types. """
        pass

    @abstractmethod
    def generate(self):
        """ generate objects in blender to link the data. """
        pass

    @abstractmethod
    def animate(self):
        """ apply keyframes to bpy objects. """
        pass

    @abstractmethod
    def structure(self):
        """ move the data to collections or set constraints. """
        pass
