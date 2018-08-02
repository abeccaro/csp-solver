class Problem:

    def __init__(self, vars = [], constrs = []):
        self.variables = vars
        self.constraints = constrs


    def add_variable(self, var):
            self.variables.append(var)

    def add_constraint(self, constr):
        self.constraints.append(constr)


    def is_solution(self, assignment):
        if len(self.variables) != len(assignment):
            return False

        for c in self.constraints:
            if not c.satisfied(assignment):
                return False

        return True