from csp.constraints.constraint import Constraint

class AllDiff(Constraint):

    # vars is a list of variables names
    def __init__(self, vars):
        self.vars = vars


    def satisfied(self, assignment):
        s = set()
        for var in self.vars:
            if var not in assignment.assignments or assignment.assignments[var] in s:
                return False
            s.add(assignment.assignments[var])
        return True