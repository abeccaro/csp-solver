from copy import deepcopy
from csp.assignment import Assignment
from csp.solvers.solver import Solver

class BacktrackSolver(Solver):

    def solve(self, problem):
        return self.__solve_recursive(problem, Assignment())


    def __solve_recursive(self, problem, assignment):
        if problem.is_solution(assignment):
            return assignment

        if len(assignment) == len(problem.variables):
            return None

        # Get an unassigned variable
        # TODO: implement different variable orders (strategy pattern)
        i = 0
        v = problem.variables[i]
        while v.name in assignment.assignments:
            i += 1
            v = problem.variables[i]

        # TODO: order v.domain (strategy pattern)
        for value in v.domain:
            # make new assignment v = value
            new_assignment = deepcopy(assignment)
            new_assignment.assign(v.name, value)

            # inference
            # TODO: implement inferences (strategy pattern)
            # new_assignment = problem.inference(new_assignment, v)

            # check consistency
            # TODO: implement node/arc/k consistency (strategy pattern)
            # if not problem.consistentAssignment(new_assignment, v):
                # continue

            # recursive call and eventual solution return
            solution = self.__solve_recursive(problem, new_assignment)
            if solution is not None:
                return solution

        # if here no assignment is valid
        return None
