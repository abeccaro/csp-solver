from csp.constraints.constraint import Constraint

class AllDiff(Constraint):
    """Class that represents Alldiff constraint.

    The Alldiff constraint is satisfied if all considered variables assume different values.

    :param vars: A list of the names of the variables this constraint relies on
    :type vars: list
    """

    # vars is a list of variables names
    def __init__(self, vars):
        super(AllDiff, self).__init__(vars)


    def satisfied(self, assignment):
        s = set()
        for var in self.vars:
            if var not in assignment.assignments or assignment.assignments[var] in s:
                return False
            s.add(assignment.assignments[var])
        return True

    def remove_inconsistent_values(self, assignment, updated):
        if updated in self.vars:
            value = assignment.assignments[updated]
            for v in self.vars:
                if v != updated and value in assignment.domains[v]:
                    assignment.remove_from_domain(v, value)
