from abc import ABC, abstractmethod

class VariableSelection(ABC):

    @abstractmethod
    def next_var(self, assignment):
        pass