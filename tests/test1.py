import unittest
from copy import copy

from csp import *


class Test(unittest.TestCase):

    def test_sample(self):
        d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        vars = []
        constraints = []

        # rows and columns constraints
        for i in range(9):
            row_vars = []
            col_vars = []
            for j in range(9):
                name = str(i+1) + ', ' + str(j+1)
                vars.append(Variable(name, copy(d)))

                row_vars.append(name)
                col_vars.append(str(j+1) + ', ' + str(i+1))
            constraints.append(AllDiff(row_vars))
            constraints.append(AllDiff(col_vars))

        # TODO: squares constraints

        prob = Problem(vars, constraints)

        inf = ForwardChecking()
        solver = BacktrackSolver(inf)

        print('Solution:\n')
        print(solver.solve(prob))
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()