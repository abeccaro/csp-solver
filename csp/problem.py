class Problem:
    """Class that represents a csp problem.

    :param vars: The variables of the problem
    :param constraints: The constraints
    :type vars: list
    :type constraints: list
    """

    def __init__(self, vars = None, constraints = None):
        if constraints is None:
            constraints = []
        if vars is None:
            vars = []

        self.variables = vars
        self.constraints = constraints


    def add_variable(self, var):
        """Adds a variable to this problem.

        :param var: The variable to add
        :type var: Variable
        """
        self.variables.append(var)

    def add_constraint(self, constr):
        """Adds a constraint to this problem.

        :param constr: The constraint to add
        :type constr: Constraint
        """
        self.constraints.append(constr)

    def remove_constraint(self, constr):
        """Removes a constraint from this problem.

        :param constr: The constraint to remove
        :type constr: Constraint
        """
        self.constraints.remove(constr)


    def is_solution(self, assignment):
        """Checks if given assignment is a solution for this problem.

        Partial assignments won't be considered solutions even if all constraints are satisfied.

        :param assignment: The assignment to check
        :type assignment: Assignment
        :return: True if assignment is a solution, False otherwise
        :rtype: bool
        """
        if len(self.variables) != len(assignment):
            return False

        for c in self.constraints:
            if not c.satisfied(assignment):
                return False

        return True