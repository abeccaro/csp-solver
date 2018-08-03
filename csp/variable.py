class Variable:
    """Class that represents a csp variable.

    :param name: The variable name
    :param domain: The variable domain
    :type name: str
    :type domain: list
    """

    def __init__(self, name, domain):
        self.name = name
        self.domain = domain