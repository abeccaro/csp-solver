from abc import ABC, abstractmethod

class Constraint(ABC):
    """Abstract class that models a constraint.

    :param vars: A list of the names of the variables this constraint relies on
    :type vars: list
    """

    @abstractmethod
    def __init__(self, vars):
        self.vars = vars


    @abstractmethod
    def satisfied(self, assignment):
        """Checks if this constraint is satisfied by given assignment

        :param assignment: The assignment
        :type assignment: Assignment
        :return: True if constraint is satisfied, false otherwise
        :rtype: bool
        """
        pass

    @abstractmethod
    def remove_inconsistent_values(self, assignment, updated):
        """Removes inconsistent values from given assignment after 'updated' variable was updated

        This is called when inference is done

        :param assignment: The current assignment
        :param updated: The name of the updated variable
        :type assignment: Assignment
        :type updated: str
        """
        pass
