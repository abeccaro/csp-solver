from csp.constraints.constraint import Constraint

class DiffNotEqualValue(Constraint):
    """Class that represents a constraint of type X - Y =/= k.

    :param var1: The name of first variable
    :param var2: The name of second variable
    :param value: The value that difference should assume
    :type var1: str
    :type var2: str
    """

    def __init__(self, var1, var2, value):
        super(DiffNotEqualValue, self).__init__([var1, var2])
        self._value = value


    def satisfied(self, assignment):
        v1 = assignment.assignments[self.vars[0]]
        v2 = assignment.assignments[self.vars[1]]
        if v1 - v2 != self._value:
            return True
        return False

    def remove_inconsistent_values(self, assignment, updated):
        if updated == self.vars[0]: # updated var1
            if self.vars[0] in assignment.assignments:
                value1 = assignment.assignments[self.vars[0]]
                assignment.remove_from_domain(self.vars[1], value1 - self._value)
        else: #updated var2
            if self.vars[1] in assignment.assignments:
                value2 = assignment.assignments[self.vars[1]]
                assignment.remove_from_domain(self.vars[0], value2 - self._value)
