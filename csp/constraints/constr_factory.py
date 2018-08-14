from csp import Variable

from csp.constraints.all_diff import AllDiff
from csp.constraints.x_equals_y import XEqualsY
from csp.constraints.x_equals_k import XEqualsK
from csp.constraints.diff_not_equal_k import DiffNotEqualK
from csp.constraints.operator import Operator


__constr_id = -1


def _constr_id():
    """Returns next constraint id."""
    global __constr_id
    
    __constr_id += 1
    return __constr_id


def all_diff(vars, name=None):
    """Creates an AllDiff constraints with given variables.
    
    :param name: The constraint name
    :param vars: The variables
    :type name: str
    :type vars: list of Variable
    :return: The AllDiff constraint
    :rtype: AllDiff
    """
    if name is None:
        name = 'c' + str(_constr_id())
    
    return AllDiff(name, vars)
    
def arithmetic(v1, op1, v2, op2=None, v3=None, name=None):
    """Creates a constraint based on given expression.
    
    Constraints can be of type:
    X op k
    X op Y
    X op1 Y op2 k, with op1 arithmetic and op2 comparison
    where X, Y are variables and k is a constant expression
    
    :return: The constraint representing given expression
    :rtype: Constraint
    """
    err = ValueError('Incorrect formula for constraint')
    
    if name is None:
        name = 'c' + str(_constr_id())
    
    if op2 is None:
        if isinstance(v2, Variable):  # var1 op1 var2
            if op1 is Operator.eq:  # X = Y
                return XEqualsY(name, v1, v2)
            elif op1 is Operator.ne:  # X != Y
                raise NotImplementedError()
            elif op1 is Operator.lt:  # X < Y
                raise NotImplementedError()
            elif op1 is Operator.le:  # X <= Y
                raise NotImplementedError()
            elif op1 is Operator.gt:  # X > Y
                raise NotImplementedError()
            elif op1 is Operator.ge:  # X >= Y
                raise NotImplementedError()
            else:
                raise err

        else:  # var1 op1 val
            if op1 is Operator.eq:  # X = k
                return XEqualsK(name, v1, v2)
            elif op1 is Operator.ne:  # X != Y
                raise NotImplementedError()
            elif op1 is Operator.lt:  # X < Y
                raise NotImplementedError()
            elif op1 is Operator.le:  # X <= Y
                raise NotImplementedError()
            elif op1 is Operator.gt:  # X > Y
                raise NotImplementedError()
            elif op1 is Operator.ge:  # X >= Y
                raise NotImplementedError()
            else:
                raise err

    else:  # var1 op1 var2 op2 val
        if op1 is Operator.plus:
            if op2 is Operator.eq:  # X + Y = k
                raise NotImplementedError()
            if op2 is Operator.ne:  # X + Y != k
                raise NotImplementedError()
            if op2 is Operator.lt:  # X + Y < k
                raise NotImplementedError()
            if op2 is Operator.le:  # X + Y <= k
                raise NotImplementedError()
            if op2 is Operator.gt:  # X + Y > k
                raise NotImplementedError()
            if op2 is Operator.ge:  # X + Y >= k
                raise NotImplementedError()
            else:
                raise err
        elif op1 is Operator.minus:
            if op2 is Operator.eq:  # X - Y = k
                raise NotImplementedError()
            if op2 is Operator.ne:  # X - Y != k
                return DiffNotEqualK(name, v1, v2, v3)
            if op2 is Operator.lt:  # X - Y < k
                raise NotImplementedError()
            if op2 is Operator.le:  # X - Y <= k
                raise NotImplementedError()
            if op2 is Operator.gt:  # X - Y > k
                raise NotImplementedError()
            if op2 is Operator.ge:  # X - Y >= k
                raise NotImplementedError()
            else:
                raise err
        else:
            raise err
