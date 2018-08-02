from csp.var_select.variable_selection import VariableSelection

class DefaultOrder(VariableSelection):

    def next_var(self, assignment):
        for var in assignment.domains:
            if var not in assignment.assignments:
                return var

        print('Error: called next_var when all variables are already assigned')