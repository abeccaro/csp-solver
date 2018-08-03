from copy import deepcopy

class Assignment:
    """Class that represents an assignment of variables.

    It also stores domains (possibly reduced from beginning of search) of all variables

    :param vars: The list of Variables to consider
    :type vars: list
    :var domains: domain for each considered variable
    :type domains: dict
    """

    def __init__(self, vars = None):
        if vars is None:
            vars = []

        self.assignments = {}
        self.domains = {}
        for v in vars:
            self.domains[v.name] = v.domain


    def __len__(self):
        """Returns the number of assigned variables

        :return: The number of assigned variables
        """
        return len(self.assignments)

    def __str__(self):
        """Return a string representation of this assignment

        :return: The string representation of this assignment
        """
        s = ''
        for var in sorted(self.domains):
            if var in self.assignments:
                s += var + ' = ' + str(self.assignments[var]) + '\n'
            else:
                s += var + ' = ' + str(self.domains[var]) + '\n'
        return s

    def __deepcopy__(self, memo):
        """Creates and returns a deep copy of this assignment

        :param memo: Memo dictionary with object ids
        :type memo: dict
        :return: A deep copy of this assignment
        """
        copy = Assignment()
        copy.assignments = deepcopy(self.assignments)
        copy.domains = deepcopy(self.domains)
        return copy


    def assign(self, name, value):
        """Makes a new assignment of a variable.

        This doesn't check if variable is already assigned.
        It also updates domain to only contain given value

        :param name: The name of the variable to assign
        :param value: The value to assign
        :type name: str
        """
        self.assignments[name] = value
        self.update_domain(name, [value])

    def update_domain(self, name, domain):
        """Changes the domain of a variable with given one.

        :param name: The name of the variable
        :param domain: The new domain
        :type name: str
        :type domain: list
        """
        self.domains[name] = domain

    def remove_from_domain(self, name, value):
        """Removes specified value from the domain of a variable.

        :param name: The name of the variable
        :param value: The value to remove
        :type name: str
        """
        self.domains[name].remove(value)