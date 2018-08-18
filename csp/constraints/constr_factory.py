from csp import Variable

from csp.constraints.operator import Operator

from csp.constraints.all_diff import AllDiff

from csp.constraints.x_equals_k import XEqualsK
from csp.constraints.x_not_equal_k import XNotEqualK
from csp.constraints.x_less_or_equal_k import XLessOrEqualK
from csp.constraints.x_greater_or_equal_k import XGreaterOrEqualK

from csp.constraints.sum_equals_k import SumEqualsK
from csp.constraints.sum_not_equal_k import SumNotEqualK
from csp.constraints.sum_less_or_equal_k import SumLessOrEqualK
from csp.constraints.sum_greater_or_equal_k import SumGreaterOrEqualK

from csp.constraints.diff_equals_k import DiffEqualsK
from csp.constraints.diff_not_equal_k import DiffNotEqualK
from csp.constraints.diff_less_or_equal_k import DiffLessOrEqualK


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
    X op1 Y op2 k
    where X, Y are variables and k is a value.
    Expression should have 1 and only 1 comparison operator.
    
    :param v1: The first variable X
    :param op1: The operator between v1 and v2
    :param v2: The second variable Y for binary constraints or the value k for unary constraints
    :param op2: The operator between v2 and v3
    :param v3: The value k
    :param name: The name of the constraint
    :type v1: IntVariable
    :type op1: Operator
    :type v2: IntVariable for binary constraints or int for unary constraints
    :type op2: Operator
    :type v3: int
    :return: The constraint representing given expression
    :rtype: Constraint
    """
    err = ValueError('Incorrect formula for constraint')
    
    if name is None:
        name = 'c' + str(_constr_id())
    
    if op2 is None:
        if isinstance(v2, Variable):  # var1 op1 var2
            if op1 is Operator.eq:  # X = Y --> X - Y = 0
                return DiffEqualsK(name, v1, v2, 0)
            elif op1 is Operator.ne:  # X != Y --> X - Y != 0
                return DiffNotEqualK(name, v1, v2, 0)
            elif op1 is Operator.lt:  # X < Y --> X - Y <= -1
                return DiffLessOrEqualK(name, v1, v2, -1)
            elif op1 is Operator.le:  # X <= Y --> X - Y <= 0
                return DiffLessOrEqualK(name, v1, v2, 0)
            elif op1 is Operator.gt:  # X > Y --> Y - X <= -1
                return DiffLessOrEqualK(name, v1, v2, -1)
            elif op1 is Operator.ge:  # X >= Y --> Y - X <= 0
                return DiffLessOrEqualK(name, v2, v1, 0)

        else:  # var1 op1 val
            if op1 is Operator.eq:  # X = k
                return XEqualsK(name, v1, v2)
            elif op1 is Operator.ne:  # X != k
                return XNotEqualK(name, v1, v2)
            elif op1 is Operator.lt:  # X < k --> X <= k-1
                return XLessOrEqualK(name, v1, v2 - 1)
            elif op1 is Operator.le:  # X <= k
                return XLessOrEqualK(name, v1, v2)
            elif op1 is Operator.gt:  # X > k --> X >= k+1
                return XGreaterOrEqualK(name, v1, v2 + 1)
            elif op1 is Operator.ge:  # X >= k
                return XGreaterOrEqualK(name, v1, v2)

    else:  # var1 op1 var2 op2 val
        if op1 is Operator.plus:
            if op2 is Operator.eq:  # X + Y = k
                return SumEqualsK(name, v1, v2, v3)
            if op2 is Operator.ne:  # X + Y != k
                return SumNotEqualK(name, v1, v2, v3)
            if op2 is Operator.lt:  # X + Y < k --> X + Y <= k-1
                return SumLessOrEqualK(name, v1, v2, v3 - 1)
            if op2 is Operator.le:  # X + Y <= k
                return SumLessOrEqualK(name, v1, v2, v3)
            if op2 is Operator.gt:  # X + Y > k --> X + Y >= k+1
                return SumGreaterOrEqualK(name, v1, v2, v3 + 1)
            if op2 is Operator.ge:  # X + Y >= k
                return SumGreaterOrEqualK(name, v1, v2, v3)

        elif op1 is Operator.minus:
            if op2 is Operator.eq:  # X - Y = k
                return DiffEqualsK(name, v1, v2, v3)
            if op2 is Operator.ne:  # X - Y != k
                return DiffNotEqualK(name, v1, v2, v3)
            if op2 is Operator.lt:  # X - Y < k --> X - Y <= k-1
                return DiffLessOrEqualK(name, v1, v2, v3 - 1)
            if op2 is Operator.le:  # X - Y <= k
                return DiffLessOrEqualK(name, v1, v2, v3)
            if op2 is Operator.gt:  # X - Y > k --> Y - X <= -(k - 1)
                return DiffLessOrEqualK(name, v2, v1, -(v3 + 1))
            if op2 is Operator.ge:  # X - Y >= k --> Y - X <= -k
                return DiffLessOrEqualK(name, v2, v1, -v3)

        elif not op2.is_comparison_op():
            new_val = v3 if op2 is Operator.plus else -v3
            return arithmetic(v1, Operator.minus, v2, op1, new_val)

    raise err
