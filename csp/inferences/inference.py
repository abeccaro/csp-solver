from abc import ABC, abstractmethod

class Inference(ABC):

    @abstractmethod
    def infer(self, assignment, constraints, updated):
        pass