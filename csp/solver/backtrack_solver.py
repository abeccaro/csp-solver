import time

from csp.solver import Solver
from csp import ContradictionException, ArcConsistencyPropagator, MinRemainingValues, SearchStatistics


class BacktrackSolver(Solver):
    """Implementation of a csp solver using backtracking search.
    
    :param prop: The constraint propagator to use
    :type prop: Propagator
    """
    
    def __init__(self, prop=ArcConsistencyPropagator(), var_ordering=MinRemainingValues()):
        super().__init__(prop, var_ordering)
    
    
    def _solve(self, problem):
        stats = SearchStatistics()
        start = time.time()

        # initial propagation
        for v in problem.variables:
            if v.domain_size() == 1:
                v.instantiate_to(v.domain[0])
            else:
                v.notify()
        
        # starting recursive search
        solved = self._solve_recursive(problem, stats)

        stats.time = time.time() - start
        return solved, stats
    
    def _solve_recursive(self, problem, stats):
        """Solves given problem using backtracking logic.
        
        :param problem: The problem to solver
        :param stats: The search statistics to update
        :type problem: Problem
        :type stats: SearchStatistics
        :return: True if problem has been solved, False otherwise
        :rtype: bool
        """
        # checking if problem is solved
        if problem.is_solved():
            stats.explored += 1
            return True
        
        # choosing next variable to instantiate
        var = self.var_ordering.next_var()
        
        if var is None:  # if all variables are already instantiated
            stats.explored += 1
            return False
        
        # for each possible value of var
        dom = var.ordered_domain()
        for value in dom:

            # push state for backtracking
            for v in problem.variables:
                v.push_state()
                
            try:
                # instantiate var = value and propagate
                var.instantiate_to(value)
            except ContradictionException:
                # backtrack and try next value
                self._backtrack(var, value, stats, problem.variables)
                continue
            
            # recursive search
            solved = self._solve_recursive(problem, stats)
            
            if solved:
                return True
            
            self._backtrack(var, value, stats, problem.variables)
        
        # if no value of var leads to a solution, fail
        return False

    @staticmethod
    def _backtrack(var, value, stats, all_vars):
        for v in all_vars:
            v.pop_state()

        try:
            var.remove_value(value, False)
        except ContradictionException:
            pass

        stats.backtracks += 1
