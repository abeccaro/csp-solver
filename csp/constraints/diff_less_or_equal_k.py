from csp.constraints.constraint import Constraint

class DiffLessOrEqualK(Constraint):
    """Constraint for expressions of type x - y <= k.
    
    :param name: The name
    :param var1: The first variable
    :param var2: The second variable
    :param value: The value
    :type name: str
    :type var1: IntVariable
    :type var2: IntVariable
    :type value: int
    """
    
    def __init__(self, name, var1, var2, value):
        super().__init__(name)
        self.var1 = var1
        self.var2 = var2
        self.value = value
    
    
    def get_vars(self):
        return [self.var1, self.var2]
    
    def is_satisfied(self):
        val1 = self.var1.get_value()
        val2 = self.var2.get_value()
        if val1 is None or val2 is None:
            return False
        
        return val1 - val2 <= self.value
    
    def propagate(self, var):
        if var is self.var1:
            # y >= x - k --> y.lb = x.lb - k
            self.var2.update_lb(self.var1.lb - self.value)
        else:  # var is self.var2
            # x <= y + k --> x.ub = y.ub + k
            self.var1.update_ub(self.var2.ub + self.value)
