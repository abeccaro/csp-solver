from csp.propagators.propagator import Propagator


class ArcConsistencyPropagator(Propagator):
    """Propagator that applies forward checking."""
    
    def __init__(self):
        super().__init__()

    
    def on_domain_change(self, var):
        if self.enabled:
            for c in self.map[var]:
                c.propagate(var)
