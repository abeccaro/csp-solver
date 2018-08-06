from copy import deepcopy
import time

from csp.solvers.solver import Solver
from csp.solvers.search_stats import SearchStats
from csp import Assignment
from csp.inferences import NoInference
from csp.var_select import DefaultOrder

class BacktrackSolver(Solver):
    """Solver implementation for backtracking search.

    :param inference: The inference strategy, defaults to NoInference
    :param var_select: The strategy to select next variable to assign
    :type inference: Inference
    :type var_select: VariableSelection
    """

    def __init__(self, inference = NoInference(), var_select = DefaultOrder()):
        self._inference = inference
        self._var_select = var_select


    def solve(self, problem):
        stats = SearchStats()
        start = time.time()

        a = Assignment(problem.variables)

        # apply node consistency and delete unary constraints
        for c in problem.constraints:
            if len(c.vars) == 1:
                c.remove_inconsistent_values(a, '')
                problem.remove_constraint(c)

        # assigning all variables that have only one possible value
        for v in a.domains:
            if len(a.domains[v]) == 1:
                a.assign(v, a.domains[v][0])
                self._inference.infer(a, problem.constraints, v)

        # calling recursive search procedure
        sol = self._solve_recursive(problem, a, stats)

        stats.time = time.time() - start

        if sol is None:
            return None, stats
        return sol.assignments, stats


    def _solve_recursive(self, problem, assignment, stats):
        """Solves given problem starting from given assignment.

        This method actually implements the backtracking logic, so it performs success or fail detection and variables
        assignment with backtracking.

        :param problem: The problem to solve
        :param assignment: The starting assignment
        :param stats: The search stats
        :type problem: Problem
        :type assignment: Assignment
        :type stats: SearchStats
        :return: The solution or None
        :rtype: Assignment
        """
        # checks if current assignment is a solution
        if problem.is_solution(assignment):
            return assignment

        # if all variables are assigned but 'assignment' is not a solution then fail
        if len(assignment) == len(problem.variables):
            stats.explored_sol += 1
            return None

        # Get an unassigned variable
        v = self._var_select.next_var(assignment)

        # cycling on possible values of chosen variable 'v'
        for value in assignment.domains[v]:
            # make new assignment v = value
            new_assignment = deepcopy(assignment) # need copy for backtracking
            new_assignment.assign(v, value)

            # inference
            self._inference.infer(new_assignment, problem.constraints, v)

            # if at least one domain is empty there's no solution with 'new_assignment'
            for d in new_assignment.domains:
                if len(d) == 0:
                    return None

            # recursive call and eventual solution return
            solution = self._solve_recursive(problem, new_assignment, stats)
            if solution is not None:
                return solution

            stats.backtracks += 1

        # if this point is reached there's no solution with given assignment
        return None
