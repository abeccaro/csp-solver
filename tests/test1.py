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


        inf = ForwardChecking()
        solver = BacktrackSolver(inf)

        print('Solution:')
        print(solver.solve(prob))
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()