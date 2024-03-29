from csp.constraints.constraint import Constraint

class XGreaterOrEqualK(Constraint):
    """Constraint for expressions of type x >= k.
    
    :param name: The name
    :param var: The variable
    :param val: The value
    :type name: str
    :type var: IntVariable
    :type val: int
    """
    
    def __init__(self, name, var, val):
        super().__init__(name)
        self.var = var
        self.val = val
    
    
    def get_vars(self):
        return [self.var]
    
    def is_satisfied(self):
        return self.var.get_value() >= self.val
    
    def propagate(self, var):
        self.var.update_lb(self.val)
