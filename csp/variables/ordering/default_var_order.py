from csp.variables.ordering.var_ordering_strategy import VarOrderingStrategy


class DefaultVarOrder(VarOrderingStrategy):
    """Implementation of variable ordering strategy that keeps default order."""

    def __init__(self):
        super().__init__()


    def next_var(self):
        for v in self.vars:
            if not v.is_instantiated():
                return v

        return None
