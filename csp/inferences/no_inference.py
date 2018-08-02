from csp.inferences.inference import Inference

class NoInference(Inference):

    def infer(self, assignment, constraints, updated):
        pass