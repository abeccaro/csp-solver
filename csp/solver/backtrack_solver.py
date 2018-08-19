from csp.solver import Solver
from csp import ContradictionException, ArcConsistencyPropagator, MinRemainingValues


class BacktrackSolver(Solver):
    """Implementation of a csp solver using backtracking search.
    
    :param prop: The constraint propagator to use
    :type prop: Propagator
    """
    
    def __init__(self, prop=ArcConsistencyPropagator(), var_ordering=MinRemainingValues()):
        super().__init__(prop, var_ordering)
    
    
    def _solve(self, problem):
        # initial propagation
        for v in problem.variables:
            v.notify()
        
        # starting search
        return self._solve_recursive(problem)
    
    def _solve_recursive(self, problem):
        """Solves given problem using backtracking logic.
        
        :param problem: The problem to solver
        :type problem: Problem
        :return: True if problem has been solved, False otherwise
        :rtype: bool
        """
        # checking if problem is solved
        if problem.is_solved():
            return True
        
        # choosing next variable to instantiate
        var = self.var_ordering.next_var()
        
        if var is None:  # if all variables are already instantiated
            return False
        
        # choosing value to instantiate var to
        # TODO: implement domain ordering strategies
        for value in var:
            # push state for backtracking
            for v in problem.variables:
                v.push_state()
                
            try:
                # instantiate var = value and propagate
                var.instantiate_to(value)
            except ContradictionException:
                # backtrack and try next value
                for v in problem.variables:
                    v.pop_state()
                continue
            
            # recursive search
            solved = self._solve_recursive(problem)
            
            if solved:
                return True
            
            # backtrack
            for v in problem.variables:
                v.pop_state()
        
        # if no value of var leads to a solution, fail
        return False
