from csp.variables.ordering.var_ordering_strategy import VarOrderingStrategy


class MinRemainingValues(VarOrderingStrategy):
    """Implementation of variable ordering strategy that orders by domain size (ascending)."""

    def __init__(self):
        super().__init__()
        self.map = {}

    def setup(self, problem):
        """Called to initialize this propagator with problem data

        :param problem: The csp
        :type problem: Problem
        """
        super().setup(problem)

        for v in self.vars:
            self.map[v] = []

        for c in problem.constraints:
            for v in c.get_vars():
                self.map[v].append(c)


    def next_var(self):
        self.vars.sort(key=lambda v: (v.domain_size(), -len(self.map[v])))

        for v in self.vars:
            if not v.is_instantiated():
                return v

        return None
