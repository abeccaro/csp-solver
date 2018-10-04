from csp.contradiction_exception import ContradictionException
from csp.variables.domain_ordering.domain_ordering_strategy import DomainOrderingStrategy


class LeastConstrainingValue(DomainOrderingStrategy):
    """Implementation of least constraining value strategy.

    This strategy returns the value that rules out the fewest choices for the neighboring variables.
    """

    def __init__(self):
        super().__init__()
        self.constraints = []  # list of self.var constraints


    def setup(self, problem, propagator):
        for c in problem.constraints:
            if self.var in c.get_vars():
                self.constraints.append(c)


    def ordered_domain(self):
        counts = []

        for value in self.var.domain:
            removed = 0

            for c in self.constraints:
                removed += c.count_removals(self.var, value)

            # appending to calculated lists
            counts.append((removed, value))

        # sorting by neighbours remaining values
        counts.sort()
        return [v for _, v in counts]
