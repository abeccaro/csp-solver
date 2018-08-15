from csp.propagators.propagator import Propagator
from csp import ContradictionException


class ArcConsistencyPropagator(Propagator):
    """Propagator that applies forward checking."""
    
    def __init__(self):
        super().__init__()
        self.first = None
        self.queue = []
        self.propagating_first = False


    def _reset(self):
        """Resets this propagator"""
        self.first = None
        self.queue = []
        self.propagating_first = False

    def _propagate_var(self, var):
        """Propagates all constraints relative to given variable assuring state remains consistent.

        :param var: The variable
        :type var: Variable
        """
        if var in self.map:
            for c in self.map[var]:
                try:
                    c.propagate(var)
                except ContradictionException:
                    self._reset()
                    raise
    
    def on_domain_change(self, var):
        if self.first is None:  # propagation starting
            self.first = var

            # propagate var
            self.propagating_first = True
            self._propagate_var(var)
            self.propagating_first = False

            # then propagate queue
            for v in self.queue:
                self._propagate_var(v)

            # reset status
            self._reset()

        elif self.propagating_first:  # propagating first variable
            if var not in self.queue:
                self.queue.append(var)

        # else do nothing
