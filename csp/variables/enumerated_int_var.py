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

        
    def instantiate_to(self, value):
        self._values = [value]
        super().instantiate_to(value)
    
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
    
    def __rem_val(self, value):
        """Same as remove_value but doesn't notify observers.
        
        This is used as subroutine in all value removing functions.
        
        :param value: The value to remove
        :type value: int
        :return: True if value was actually removed, False otherwise
        :rtype: bool
        :raise: ContradictionException: If domain wipeout happens
        """
        if self.contains(value):
            self._values.remove(value)
            
            if self.domain_size() == 0:
                raise ContradictionException(self.name + ' domain wipeout, removed last value: ' + str(value))
                
            if value == self.lb:
                self.update_lb(min(self._values))
            if value == self.ub:
                self.update_ub(max(self._values))
            
            return True
        return False
    
    def remove_value(self, value):
        removed = self.__rem_val(value)
        if removed:
            self.notify()
        return removed
    
    def remove_values(self, values):
        removed = False
        for v in values:
            removed = removed or self.__rem_val(v)
        
        if removed:
            self.notify()
        
        return removed
    
    def remove_range(self, start, end):
        if end - start < self.domain_size():
            return self.remove_values(range(start, end + 1))
        
        removed = False
        for v in self._values:
            if start <= v <= end:
                removed = self.__rem_val(v)  # always true as we are iterating through domain elements
        if removed:
            self.notify()
        return removed
    
    def keep_only_values(self, values):
        removed = False
        old_len = self.domain_size()
        
        self._values[:] = [v for v in self._values if v in values]
        
        if old_len > self.domain_size():
            removed = True
            self.notify()
                
        return removed
    
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
