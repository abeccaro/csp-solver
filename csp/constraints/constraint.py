from abc import ABC, abstractmethod

class Constraint(ABC):

    def __init__(self):
        self.vars = []


    @abstractmethod
    def satisfied(self, assignment):
        pass

    @abstractmethod
    def remove_inconsistent_values(self, assignment, updated):
        pass
