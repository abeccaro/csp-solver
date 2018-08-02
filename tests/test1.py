import unittest
from copy import copy

from csp import *


class Test(unittest.TestCase):

    def test_sample(self):
        prob = Problem()

        #variables
        d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            for j in range(9):
                vij = Variable(str(i+1) + ',' + str(j+1), copy(d))
                prob.add_variable(vij)

        #constraints
        #rows and cols
        for i in range(9):
            row_vars = []
            col_vars = []
            for j in range(9):
                row_vars.append(str(i+1)+','+str(j+1))
                col_vars.append(str(j+1)+','+str(i+1))
            prob.add_constraint(AllDiff(row_vars))
            prob.add_constraint(AllDiff(col_vars))

        #squares constraints
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                square_vars = []
                for k in range(3):
                    for l in range(3):
                        square_vars.append(str(i+k)+','+str(j+l))
                prob.add_constraint(AllDiff(square_vars))


        prob.add_constraint(EqualsValue('1,2', 5))
        prob.add_constraint(EqualsValue('1,3', 2))
        prob.add_constraint(EqualsValue('1,4', 6))
        prob.add_constraint(EqualsValue('1,7', 4))
        prob.add_constraint(EqualsValue('1,8', 8))

        prob.add_constraint(EqualsValue('3,1', 4))
        prob.add_constraint(EqualsValue('3,2', 9))
        prob.add_constraint(EqualsValue('3,4', 7))
        prob.add_constraint(EqualsValue('3,5', 8))
        prob.add_constraint(EqualsValue('3,6', 3))
        prob.add_constraint(EqualsValue('3,8', 6))
        prob.add_constraint(EqualsValue('3,9', 2))

        prob.add_constraint(EqualsValue('4,3', 5))
        prob.add_constraint(EqualsValue('4,5', 4))
        prob.add_constraint(EqualsValue('4,7', 8))
        prob.add_constraint(EqualsValue('4,9', 9))

        prob.add_constraint(EqualsValue('5,3', 6))
        prob.add_constraint(EqualsValue('5,7', 7))

        prob.add_constraint(EqualsValue('6,1', 2))
        prob.add_constraint(EqualsValue('6,3', 3))
        prob.add_constraint(EqualsValue('6,5', 7))
        prob.add_constraint(EqualsValue('6,7', 1))

        prob.add_constraint(EqualsValue('7,1', 1))
        prob.add_constraint(EqualsValue('7,2', 2))
        prob.add_constraint(EqualsValue('7,4', 5))
        prob.add_constraint(EqualsValue('7,5', 3))
        prob.add_constraint(EqualsValue('7,6', 9))
        prob.add_constraint(EqualsValue('7,8', 7))
        prob.add_constraint(EqualsValue('7,9', 4))

        prob.add_constraint(EqualsValue('9,2', 7))
        prob.add_constraint(EqualsValue('9,3', 9))
        prob.add_constraint(EqualsValue('9,6', 8))
        prob.add_constraint(EqualsValue('9,7', 3))
        prob.add_constraint(EqualsValue('9,8', 5))


        inf = ForwardChecking()
        var_sel = MinRemainingValues()
        solver = BacktrackSolver(inf, var_sel)

        solution = solver.solve(prob)

        print('Solution:')
        print(solution)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()