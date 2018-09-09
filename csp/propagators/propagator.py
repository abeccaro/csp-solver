from abc import abstractmethod

from csp.observer import Observer


class Propagator(Observer):
    """Abstract class for a constraint propagator."""
    
    def __init__(self):
        super().__init__()
        self.enabled = True
        self.map = {}
    
    
    def on_event(self, var):
        self.on_domain_change(var)
    
    @abstractmethod
    def on_domain_change(self, var):
        """Called when a variable domain has changed.
        
        :param var: The variable that changed
        :type var: Variable
        """
        pass
    
    def setup(self, problem):
        """Called to initialize this propagator with problem data

        :param problem: The csp
        :type problem: Problem
        """
        for v in problem.variables:
            v.add_observer(self)
            self.map[v] = []

        for c in problem.constraints:
            for v in c.get_vars():
                self.map[v].append(c)
