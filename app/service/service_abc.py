from abc import ABC, abstractmethod

class WorkGraphBase(ABC):
    @abstractmethod
    def add_graph(self):
        pass