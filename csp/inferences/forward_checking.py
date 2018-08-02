from csp.inferences.inference import Inference

class ForwardChecking(Inference):

    def infer(self, assignment, constraints, updated):
        for c in constraints:
            c.remove_inconsistent_values(assignment, updated)