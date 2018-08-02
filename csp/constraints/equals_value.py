from csp.constraints.constraint import Constraint

class EqualsValue(Constraint):

    def __init__(self, var, value):
        self.var = var
        self.value = value


    def satisfied(self, assignment):
        if assignment.assignments[self.var] == self.value:
            return True
        return False

    def remove_inconsistent_values(self, assignment, updated):
        if updated == self.var:
            assignment.update_domain(self.var, [self.value])
