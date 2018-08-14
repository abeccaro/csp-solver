from abc import ABC, abstractmethod


class Constraint(ABC):
    """Abstract class that represents a constraint.
    
    :param name: The name of this constraint
    :type name: str
    """
    
    def __init__(self, name):
        self.name = name
    
    
    @abstractmethod
    def get_vars(self):
        """Returns a list of the variables this constraint relies on.

        :return: The list of the variables this constraint relies on
        :rtype: list[Variable]
        """
        pass
    
    @abstractmethod
    def is_satisfied(self):
        """Checks if this constraint is satisfied with current assignments.
        
        If any variable is not instantiated yet this should return False.
        
        :return: True if constraint is satisfied, False otherwise
        :rtype: bool
        """
        pass
    
    @abstractmethod
    def propagate(self, var):
        """Adjusts each variable domain given that var domain has changed.
        
        :param var: The variable that has changed
        :type var: Variable
        """
        pass
