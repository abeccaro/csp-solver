from abc import ABC, abstractmethod

class Constraint(ABC):

    @abstractmethod
    def satisfied(self, assignment):
        pass
