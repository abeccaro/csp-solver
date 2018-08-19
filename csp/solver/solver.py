from abc import ABC, abstractmethod

from csp import ArcConsistencyPropagator, MinRemainingValues


class Solver(ABC):
    """Abstract class for a csp solver.
    
    :param prop: The constraint propagator to use
    :type prop: Propagator
    """
    
    def __init__(self, prop=ArcConsistencyPropagator(), var_ordering=MinRemainingValues()):
        self.prop = prop
        self.var_ordering = var_ordering
    
    
    def solve(self, problem):
        """Initializes solver for given problem and solves it.
        
        :param problem: The problem to solve
        :type problem: Problem
        :return: True if problem has been solved, False otherwise
        :rtype: bool
        """
        self.prop.setup(problem)
        self.var_ordering.setup(problem)
        
        return self._solve(problem)
    
    @abstractmethod
    def _solve(self, problem):
        """Solving algorithm.
        
        This is the method that should be overridden when solve process needs to be changed.
        
        :param problem: The problem to solve
        :type problem: Problem
        :return: True if problem has been solved, False otherwise
        :rtype: bool
        """
        pass
