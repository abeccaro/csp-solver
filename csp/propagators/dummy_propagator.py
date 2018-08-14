from csp.propagators.propagator import Propagator


class DummyPropagator(Propagator):
    """Propagator that actually doesn't propagate."""
    
    def on_domain_change(self, var):
        pass
