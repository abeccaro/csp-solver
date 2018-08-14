from copy import copy

from csp.variables.enumerated_int_var import EnumeratedIntVar


__var_id = -1


def _var_id():
    """Returns next variable id."""
    global __var_id

    __var_id += 1
    return __var_id


def int_var(domain=None, lb=None, ub=None, name='x' + str(_var_id())):
    """Creates an int variable from given data.
    
    If domain is given then it's used, otherwise lower and upper bounds are used and domain is [lb, ub].
    
    :param name: The name of the variable
    :param domain: The variable domain
    :param lb: The lower bound of domain values
    :param ub: The upper bound of domain values
    :type name: str
    :type lb: int
    :type ub: int
    :return: An int variable with specified domain
    :rtype: int_var
    """
    if domain is not None:
        return EnumeratedIntVar(name, copy(domain))
    return EnumeratedIntVar(name, range(lb, ub + 1))

def int_var_array(size, domain=None, lb=None, ub=None, name='x' + str(_var_id())):
    """Creates an array of int variables all with specified domain.
    
    If domain is given then it's used, otherwise lower and upper bounds are used and domain is [lb, ub].
    Variables names will be 'name[n]'.
    
    :param name: The name of the array
    :param size: The size of the array
    :param domain: The variables domain
    :param lb: The lower bound of domain values
    :param ub: The upper bound of domain values
    :type name: str
    :type size: int
    :type lb: int
    :type ub: int
    :return: A list of variables all with specified domain
    :rtype: list of int_var
    """
    vars = []
    for i in range(size):
        vars.append(int_var(domain, lb, ub, name + '[' + str(i) + ']'))
    return vars

def int_var_matrix(size1, size2, domain=None, lb=None, ub=None, name='x' + str(_var_id())):
    """Creates a matrix size1 x size2 of int variables all with specified domain.
    
    If domain is given then it's used, otherwise lower and upper bounds are used and domain is [lb, ub].
    Variables names will be 'name[row][col]'.
    
    :param name: The name of the matrix
    :param size1: The number of rows
    :param size2: The number of columns
    :param domain: The variables domain
    :param lb: The lower bound of domain values
    :param ub: The upper bound of domain values
    :type name: str
    :type size1: int
    :type size2: int
    :type lb: int
    :type ub: int
    :return: A list of lists variables all with specified domain
    :rtype: list of list of int_var
    """
    m = []
    for i in range(size1):
        row = []
        for j in range(size2):
            row.append(int_var(domain, lb, ub, name + '[' + str(i) + '][' + str(j) + ']'))
        m.append(row)
    return m
