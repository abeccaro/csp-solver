from csp.variables.domain_ordering.domain_ordering_strategy import DomainOrderingStrategy

from copy import copy


class DefaultValueOrder(DomainOrderingStrategy):
    """Implementation of variable ordering strategy that keeps default order."""

    def __init__(self):
        super().__init__()


    def ordered_domain(self):
        return copy(self.var.domain)
