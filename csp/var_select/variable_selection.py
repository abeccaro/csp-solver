from abc import ABC, abstractmethod

class VariableSelection(ABC):
    """Abstract base class for variable selection strategies."""

    @abstractmethod
    def next_var(self, assignment):
        """Chooses and returns next variable to assign.

        :param assignment: The current assignment
        :type assignment: Assignment
        """
        pass