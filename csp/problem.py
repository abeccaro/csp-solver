class Problem:

    variables = []
    constraints = []


    def __init__(self, vars, constrs):
        self.variables = vars
        self.constraints = constrs


    def is_solution(self, assignment):
        if len(self.variables) != len(assignment):
            return False

        for c in self.constraints:
            if not c.satisfied(assignment):
                return False

        return True