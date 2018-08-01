import unittest
from csp import *
from csp.solvers import *


class Test(unittest.TestCase):

    def test_sample(self):
        prob = Problem([Variable('a', [0, 1])], [])
        solver = BacktrackSolver()
        print('Solution:\n')
        print(solver.solve(prob))
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()