from csp.variables import Variable


class Problem:
    """Class that represents a csp problem."""
    
    def __init__(self):
        self.variables = []
        self.constraints = []
    
    
    def add_variable(self, to_add):
        """Adds one or more variables to this problem.
        
        It doesn't check if variables have already been added to this problem.
        
        :param to_add: The variable[s] to add
        :type to_add: Variable or list
        """
        if isinstance(to_add, Variable):
            self.variables.append(to_add)
        else:
            for x in to_add:
                self.add_variable(x)
        
    def add_constraint(self, constr):
        """Adds a constraint to this problem.
        
        It doesn't check if constraint has already been added to this problem.
        
        :param constr: The constraint to add
        :type constr: Constraint
        """
        self.constraints.append(constr)
    
    def is_solved(self):
        """Checks if this problem is solved.
        
        Partial assignment is not a solution, even if it satisfies all constraints.
        """
        for v in self.variables:
            if not v.is_instantiated():
                return False
        
        for c in self.constraints:
            if not c.is_satisfied():
                return False
        
        return True
