from csp.inferences.inference import Inference

class ForwardChecking(Inference):
    """Implementation of forward checking inference strategy.

    This strategy propagates information from assigned to unassigned variables, but doesn't provide early detection
    for all failures.
    """

    def infer(self, assignment, constraints, updated):
        for c in constraints:
            c.remove_inconsistent_values(assignment, updated)