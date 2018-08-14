from csp.constraints.constraint import Constraint

class XEqualsY(Constraint):
    """Constraint for expressions of type x = y.
    
    :param name: The name
    :param var1: The variables
    :param var2: The variables
    :type name: str
    :type var1: IntVariable
    :type var2: IntVariable
    """
    
    def __init__(self, name, var1, var2):
        super().__init__(name)
        self.var1 = var1
        self.var2 = var2
    
    
    def get_vars(self):
        return [self.var1, self.var2]
    
    def is_satisfied(self):
        val1 = self.var1.get_value()
        val2 = self.var2.get_value()
        if val1 is None:
            return False
        
        return val1 == val2
    
    def propagate(self, var):
        other = self.var2 if var == self.var1 else self.var1
        other.keep_only_values(var.domain)
