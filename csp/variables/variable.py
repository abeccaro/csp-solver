from abc import abstractmethod

from csp.observable import Observable


class Variable(Observable):
    """Abstract class that represents a variable.
    
    :param name: The name of the variable
    :type name: str
    """
    
    def __init__(self, name, domain_ordering):
        super().__init__()
        self.name = name
        self.value = None  # value, None if not yet instantiated

        self.domain_ordering = domain_ordering  # value ordering strategy
        self.domain_ordering.var = self

        self.states = []  # states to backtrack
    
    
    def is_instantiated(self):
        """Checks if this variable is instantiated."""
        return self.value is not None
    
    def instantiate_to(self, value, propagate=True):
        """Instantiate this variable to given value.
        
        Subclasses should override this method restricting domain to only 'value' and then call this using super.
        
        :param value: The value of the variable
        :param propagate: If True then propagation happens, else it doesn't
        :type propagate: bool
        """
        self.value = value
        if propagate:
            self.notify()
    
    def get_value(self):
        """Returns value if it's instantiated, otherwise None.
        
        :return: The value if it's instantiated, otherwise None
        """
        return self.value

    def ordered_domain(self):
        """Returns an ordered copy of this variable domain.

        :return: An ordered copy of this variable domain
        :rtype: list
        """
        return self.domain_ordering.ordered_domain()
    
    @abstractmethod
    def push_state(self):
        """Saves current state of the variable and pushes it into a stack.
        
        It will be used in case of backtracking to reset to previous state using 'pop_state'.
        """
        pass
    
    @abstractmethod
    def pop_state(self):
        """Loads previous state of the variable removing it from the stack.
        
        In case of empty stack a 'ContradictionException' is raised
        
        :raise: ContradictionException: if state stacks is empty
        """
        pass
