from csp.var_select.variable_selection import VariableSelection

class DefaultOrder(VariableSelection):
    """Variable select strategy that chooses the first added to the assignment"""

    def next_var(self, assignment):
        for var in assignment.domains:
            if var not in assignment.assignments:
                return var

        print('Error: called next_var when all variables are already assigned')