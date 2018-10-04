from csp.constraints.constraint import Constraint

class DiffEqualsK(Constraint):
    """Constraint for expressions of type x - y = k.
    
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
        
        return val1 - val2 == self.value
    
    def propagate(self, var):
        values = []
        if var is self.var1:
            # y = x_i - k  foreach x_i in x
            for v in var:
                values.append(v - self.value)
            self.var2.keep_only_values(values)
        else:  # var is self.var2
            # x = y_i + k  foreach y_i in y
            for v in var:
                values.append(v + self.value)
            self.var1.keep_only_values(values)

    def count_removals(self, var, val):
        if var is self.var1:
            if self.var2.contains(val - self.value):
                return self.var2.domain_size() - 1
            return self.var2.domain_size()
        else:  # var is self.var2
            if self.var1.contains(val + self.value):
                return self.var1.domain_size() - 1
            return self.var1.domain_size()