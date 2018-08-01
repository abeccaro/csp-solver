class Problem:

    variables = {}
    constraints = []


    def __init__(self, solver, vars, constrs):
        self.solver = solver
        self.variables = vars
        self.constraints = constrs


    def is_solution(self, assignment):
        if len(variables) != len(assignment):
            return false

        for c in constraints:
            if not c.satisfied(assignment):
                return false

        return true