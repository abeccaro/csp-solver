from csp.contradiction_exception import ContradictionException
from csp.variables.domain_ordering.domain_ordering_strategy import DomainOrderingStrategy


class LeastConstrainingValue(DomainOrderingStrategy):
    """Implementation of least constraining value strategy.

    This strategy returns the value that rules out the fewest choices for the neighboring variables.
    """

    def __init__(self):
        super().__init__()
        self.neighbours = []  # list of neighbour of self.var
        self.constraints = []  # list of self.var constraints

        self.propagator = None


    def setup(self, problem, propagator):
        for c in problem.constraints:
            vars = c.get_vars()
            if self.var in vars:
                for n in vars:
                    if n is not self.var and n not in self.neighbours:
                        self.neighbours.append(n)

                self.constraints.append(c)

        self.propagator = propagator


    def ordered_domain(self):
        counts = []

        for value in self.var.domain:
            # save state
            for var in self.neighbours:
                var.push_state()
            self.var.push_state()

            # applying assignment and propagating to neighbours only
            try:
                self.propagator.enabled = False

                self.var.instantiate_to(value)
                for c in self.constraints:
                    c.propagate(self.var)

                self.propagator.enabled = True
            except ContradictionException:
                # if domain wipeout happens value is put at the end
                sum = 10000000000  # FIXME: set a proper max value
                for var in self.neighbours:
                    var.pop_state()
                self.var.pop_state()

                self.propagator.enabled = True

                counts.append((sum, value))
                continue

            # calculating sum of remaining values and reverting state
            sum = 0
            for var in self.neighbours:
                sum += var.domain_size()
                var.pop_state()
            self.var.pop_state()

            # appending to calculated lists
            counts.append((sum, value))

        # sorting by neighbours remaining values
        counts.sort(reverse=True)
        return [v for _, v in counts]
