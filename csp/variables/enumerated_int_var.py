from copy import deepcopy

from csp import ContradictionException
from csp.variables.int_variable import IntVariable


class EnumeratedIntVar(IntVariable):
    """Implementation for an int variable that stores domain as a list of possible values.
    
    :param name: The name of this variable
    :param values: A collection of all possible values in domain
    :type name: str
    """
    
    def __init__(self, name, values):
        self._values = list(values)
        super(EnumeratedIntVar, self).__init__(name, min(self._values), max(self._values))

        
    def instantiate_to(self, value, propagate=True):
        self._values = [value]
        super().instantiate_to(value, propagate)
    
    @property
    def domain(self):
        return self._values
    
    def __iter__(self):
        for v in self._values:
            yield v
    
    def domain_size(self):
        return len(self._values)
    
    def contains(self, value):
        return value in self._values
    
    def remove_value(self, value, propagate=True):
        if self.contains(value):
            self._values.remove(value)

            if self.domain_size() == 0:
                raise ContradictionException(self.name + ' domain wipeout, removed last value: ' + str(value))

            if value == self.lb:
                self.update_lb(min(self._values), False)
            if value == self.ub:
                self.update_ub(max(self._values), False)

            if propagate:
                self.notify()

            return True

        return False
    
    def remove_values(self, values, propagate=True):
        old_len = self.domain_size()

        self._values[:] = [v for v in self._values if v not in values]

        if self.domain_size() == 0:
            raise ContradictionException(self.name + ' domain wipeout, removed all values')

        if self.lb in values:
            self.update_lb(min(self._values), False)
        if self.ub in values:
            self.update_ub(max(self._values), False)

        if old_len > self.domain_size():
            if propagate:
                self.notify()
            return True

        return False
    
    def remove_range(self, start, end, propagate=True):
        old_len = self.domain_size()

        self._values[:] = [v for v in self._values if v < start or v > end]

        if self.domain_size() == 0:
            raise ContradictionException(self.name + ' domain wipeout, removed all values')

        if start <= self.lb <= end:
            self.update_lb(min(self._values), False)
        if start <= self.ub <= end:
            self.update_ub(max(self._values), False)

        if old_len > self.domain_size():
            if propagate:
                self.notify()
            return True

        return False
    
    def keep_only_values(self, values, propagate=True):
        old_len = self.domain_size()
        
        self._values[:] = [v for v in self._values if v in values]

        if self.domain_size() == 0:
            raise ContradictionException(self.name + ' domain wipeout, removed all values')

        if self.lb not in values:
            self.update_lb(min(self._values), False)
        if self.ub not in values:
            self.update_ub(max(self._values), False)
        
        if old_len > self.domain_size():
            if propagate:
                self.notify()
            return True
                
        return False
    
    def push_state(self):
        self.states.append((deepcopy(self._values), self.lb, self.ub, self.value))
    
    def pop_state(self):
        if len(self.states) == 0:
            raise ContradictionException(self.name + ' has no state to backtrack')
        
        vals, lb, ub, value = self.states.pop()
        
        self._values = vals
        self._lb = lb
        self._ub = ub
        self.value = value
