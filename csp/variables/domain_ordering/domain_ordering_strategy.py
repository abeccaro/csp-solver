from abc import ABC, abstractmethod

class DomainOrderingStrategy(ABC):
    """Abstract class for a variable domain ordering strategy."""

    def __init__(self):
        self.var = None


    def setup(self, problem):
        """Called to initialize this ordering strategy with problem data.

        :param problem: The csp
        :type problem: Problem
        """
        pass

    @abstractmethod
    def ordered_domain(self):
        """Returns a copy of var domain ordered using certain strategy.

        :return: An ordered copy of var domain
        :rtype: list
        """
        pass
