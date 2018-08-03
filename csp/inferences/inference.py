from abc import ABC, abstractmethod

class Inference(ABC):
    """Abstract class for an inference strategy."""

    @abstractmethod
    def infer(self, assignment, constraints, updated):
        """Actually makes inference removing eventual inconsistent values from variable domains.

        :param assignment: The current assignment to make inference on. This will be modified
        :param constraints: The list of problem constraints
        :param updated: The name of the updated variable
        :type assignment: Assignment
        :type constraints: list
        :type updated: str
        """
        pass