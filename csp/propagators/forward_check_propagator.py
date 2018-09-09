from csp.propagators.propagator import Propagator
from csp import ContradictionException


class ForwardCheckPropagator(Propagator):
    """Propagator that applies forward checking."""
    
    def __init__(self):
        super().__init__()
        self.propagating = False

    
    def on_domain_change(self, var):
        if self.enabled:
            self.enabled = False
            
            for c in self.map[var]:
                try:
                    c.propagate(var)
                except ContradictionException:
                    self.enabled = True
                    raise
            
            self.enabled = True
