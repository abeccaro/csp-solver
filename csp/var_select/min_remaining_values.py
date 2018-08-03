from csp.var_select.variable_selection import VariableSelection

class MinRemainingValues(VariableSelection):
    """Variable selection strategy that chooses the first variable with minimum domain size"""

    def next_var(self, assignment):
        vars = list(assignment.domains)
        vars.sort(key=lambda v: len(assignment.domains[v]))
        return next(v for v in vars if v not in assignment.assignments)