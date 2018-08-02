from abc import ABC, abstractmethod

class Constraint(ABC):

    @abstractmethod
    def satisfied(self, assignment):
        pass

    @abstractmethod
    def remove_inconsistent_values(self, assignment, updated):
        pass
