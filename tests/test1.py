import unittest
from csp import *


class Test(unittest.TestCase):

    def test_sample(self):
        vars = [Variable('a', [0, 1]),
                Variable('b', [0, 1])]
        constraints = [AllDiff(['a', 'b'])]

        prob = Problem(vars, constraints)

        solver = BacktrackSolver()

        print('Solution:\n')
        print(solver.solve(prob))
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()