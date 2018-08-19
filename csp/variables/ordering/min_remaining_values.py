from csp.variables.ordering.var_ordering_strategy import VarOrderingStrategy


class MinRemainingValues(VarOrderingStrategy):
    """Implementation of variable ordering strategy that orders by domain size (ascending)."""

    def __init__(self):
        super().__init__()


    def next_var(self):
        self.vars.sort(key=lambda v: v.domain_size())

        for v in self.vars:
            if not v.is_instantiated():
                return v

        return None
