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
        :return: (solved, stats) where solved is True if problem has been solved, False otherwise and stats are search
                 statistics
        :rtype: (bool, SearchStatistics)
        """
        # apply node consistency (unary constraints)
        for c in problem.constraints[:]:
            vars = c.get_vars()
            if len(vars) == 1:
                c.propagate(vars[0])
                problem.constraints.remove(c)

        # setup strategies
        self.prop.setup(problem)
        self.var_ordering.setup(problem)
        for var in problem.variables:
            var.domain_ordering.setup(problem, self.prop)

        # call search
        return self._solve(problem)
    
    @abstractmethod
    def _solve(self, problem):
        """Solving algorithm.
        
        This is the method that should be overridden when solve process needs to be changed.
        
        :param problem: The problem to solve
        :type problem: Problem
        :return: (solved, stats) where solved is True if problem has been solved, False otherwise and stats are search
                 statistics
        :rtype: (bool, SearchStatistics)
        """
        pass
