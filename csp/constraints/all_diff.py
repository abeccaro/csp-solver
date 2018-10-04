from csp.constraints.constraint import Constraint


class AllDiff(Constraint):
    """Constraint that forces all variables to have the same value.
    
    :param name: The name
    :param vars: The variables
    :type name: str
    :type vars: list[IntVariable]
    """
    
    def __init__(self, name, vars):
        super().__init__(name)
        self.vars = vars
    
    
    def get_vars(self):
        return self.vars
    
    def is_satisfied(self):
        for i in range(len(self.vars)):
            v = self.vars[i].get_value()
            if v is None:
                return False
            for j in range(i):
                if v == self.vars[j].get_value():
                    return False
        
        return True
    
    def propagate(self, var):
        val = var.get_value()
        if val is not None:
            for v in self.vars:
                if v != var:
                    v.remove_value(val)

    def count_removals(self, var, val):
        count = 0

        for v in self.vars:
            if v is not var and v.contains(val):
                count += 1

        return count
