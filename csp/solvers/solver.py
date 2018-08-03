from abc import ABC, abstractmethod

class Solver(ABC):
    """Abstract base class for a csp solver."""

    @abstractmethod
    def solve(self, problem):
        """Finds a solution for given problem if there's one.

        In case there are no solutions None will be returned.

        :param problem: The problem to solve
        :type problem: Problem
        :return: The solution or None
        :rtype: dict
        """
        pass