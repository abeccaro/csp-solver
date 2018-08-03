from csp.constraints.constraint import Constraint

class EqualsValue(Constraint):
    """Class that represents a constraint for equality between a variable and a value.

    The EqualsValue constraint forces considered variable to assume given value.
    EqualsValue constraint is unary and as such will be processed at the beginning of solve process and will be deleted
    when it gets satisfied.

    :param var: The name of considered variable
    :param value: The value that var should assume
    :type var: str
    """

    def __init__(self, var, value):
        super(EqualsValue, self).__init__([var])
        self.var = var
        self._value = value


    def satisfied(self, assignment):
        if assignment.assignments[self.var] == self._value:
            return True
        return False

    def remove_inconsistent_values(self, assignment, updated):
        assignment.update_domain(self.var, [self._value])
