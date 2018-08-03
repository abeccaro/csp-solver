from csp.inferences.inference import Inference

class NoInference(Inference):
    """Most basic implementation of inference strategy that makes nothing."""

    def infer(self, assignment, constraints, updated):
        pass