from abc import ABC, abstractmethod
from copy import copy

class VarOrderingStrategy(ABC):
    """Abstract class for a variable ordering strategy."""

    def __init__(self):
        self.vars = []


    def setup(self, problem):
        """Called to initialize this ordering strategy with problem data

        :param problem: The csp
        :type problem: Problem
        """
        self.vars = copy(problem.variables)

    @abstractmethod
    def next_var(self):
        """Returns first non instantiated variable in strategy order.

        :return: The next non instantiated variable
        :rtype: Variable
        """
        pass
