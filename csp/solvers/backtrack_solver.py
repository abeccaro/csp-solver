from copy import deepcopy
from csp import Assignment
from csp.solvers.solver import Solver
from csp.inferences import *

class BacktrackSolver(Solver):

    def __init__(self, inference = NoInference()):
        self.inference = inference


    def solve(self, problem):
        return self.__solve_recursive(problem, Assignment(problem.variables))


    def __solve_recursive(self, problem, assignment):
        if problem.is_solution(assignment):
            return assignment

        if len(assignment) == len(problem.variables):
            return None

        # Get an unassigned variable
        # TODO: implement different variable orders (strategy pattern)
        i = 0
        v = problem.variables[i].name
        while v in assignment.assignments:
            i += 1
            v = problem.variables[i].name

        # TODO: order v.domain (strategy pattern)
        for value in assignment.domains[v]:
            # make new assignment v = value
            new_assignment = deepcopy(assignment)
            new_assignment.assign(v, value)

            # inference
            # TODO: implement other inferences (arc consistency?)
            self.inference.infer(new_assignment, problem.constraints, v)

            # check that no domain is empty
            for d in new_assignment.domains:
                if len(d) == 0:
                    return None

            # recursive call and eventual solution return
            solution = self.__solve_recursive(problem, new_assignment)
            if solution is not None:
                return solution

        # if here no assignment is valid
        return None
