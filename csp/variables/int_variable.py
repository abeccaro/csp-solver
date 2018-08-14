from abc import abstractmethod

from csp import ContradictionException
from csp.variables import Variable


class IntVariable(Variable):
    """Abstract class for integer variables.
    
    Implementations should define how domain is represented and stored.
    
    :param name: The name of this variable
    :param lb: The lower bound of domain values
    :param ub: The upper bound of domain values
    :type name: str
    :type lb: int
    :type ub: int
    """
    
    def __init__(self, name, lb, ub):
        super(IntVariable, self).__init__(name)
        self._lb = lb
        self._ub = ub
        self.update_ub(ub)  # checks feasibility of bounds
    
    
    def instantiate_to(self, value):
        self.update_bounds(value, value)
        super().instantiate_to(value)
    
    @property
    @abstractmethod
    def domain(self):
        pass
    
    @property
    def lb(self):
        """Lower bound of domain values."""
        return self._lb
    
    def update_lb(self, value):
        """Sets lb to specified value and returns True if bound is actually updated, False otherwise.
        
        :param value: The new value for lower bound
        :type value: int
        :raise: ContradictionException: If domain wipeout happens
        """
        if value <= self.lb:
            return False
        if value > self.ub:
            raise ContradictionException(self.name + ' domain wipeout: [' + str(value) + ',' + str(self.ub) + ']')
        
        self.remove_range(self.lb, value - 1)
        self._lb = value
        return True
    
    @property
    def ub(self):
        """Upper bound of domain values."""
        return self._ub
    
    def update_ub(self, value):
        """Sets ub to specified value and returns True if bound is actually updated, False otherwise.
        
        :param value: The new value for upper bound
        :type value: int
        :raise: ContradictionException: If domain wipeout happens
        """
        if value >= self.ub:
            return False
        if value < self.lb:
            raise ContradictionException(self.name + ' domain wipeout: [' + str(self.lb) + ',' + str(value) + ']')
        
        self.remove_range(value + 1, self.ub)
        self._ub = value
        return True
    
    def update_bounds(self, lb, ub):
        """Update bounds to specified values and returns True if any bound is updated, False otherwise.
        
        :param lb: The new value for lower bound
        :param ub: The new value for upper bound
        :type lb: int
        :type ub: int
        :return: True if any bound is updated, False otherwise
        :rtype: bool
        :raise: ContradictionException: If lb > ub
        """
        return self.update_lb(lb) or self.update_ub(ub)
    
    
    @abstractmethod
    def __iter__(self):
        pass
    
    @abstractmethod
    def domain_size(self):
        """Returns domain size.
        
        :return: The domain size
        :rtype: int
        """
        pass
    
    def domain_range_size(self):
        """Returns domain range size, that is ub - lb.
        
        :return: The domain range size
        :rtype: int
        """
        return self.ub - self.lb
    
    @abstractmethod
    def contains(self, value):
        """Checks if domain contains specified value.
        
        :param value: The value to check
        :type value: int
        :return: True if value is in this variable domain, False otherwise
        :rtype: bool
        """
        pass
    
    @abstractmethod
    def remove_value(self, value):
        """Removes specified value from domain if it's present.
        
        If the value is actually removed it returns True, otherwise False.
        
        :param value: The value to remove
        :type value: int
        :return: True if value was actually removed, False otherwise
        :rtype: bool
        :raise: ContradictionException: If domain wipeout happens
        """
        pass
    
    @abstractmethod
    def remove_values(self, values):
        """Removes all specified values from domain.
        
        If any value is actually removed returns True, False otherwise.
        values must be iterable.
        
        :param values: The values to remove
        :return: True if any value is actually removed, False otherwise
        :rtype: bool
        :raise: ContradictionException: If domain wipeout happens
        """
        pass
    
    @abstractmethod
    def remove_range(self, start, end):
        """Removes all values in specified range (start <= value <= end).
        
        If any value is actually removed returns True, False otherwise.
        
        :param start: the starting value inclusive
        :param end: the ending value inclusive
        :type start: int
        :type end: int
        :return: True if any value is actually removed, False otherwise
        :rtype: bool
        :raise: ContradictionException: If domain wipeout happens
        """
        pass
    
    @abstractmethod
    def keep_only_values(self, values):
        """Removes all values from domain but specified ones.
        
        values must be iterable.
        If any value is actually removed returns True, False otherwise.
        
        :param values: The values to remove
        :return: True if any value is actually removed, False otherwise
        :rtype: bool
        :raise: ContradictionException: If domain wipeout happens
        """
        pass
