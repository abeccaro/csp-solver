import unittest
from copy import copy
from pprint import pprint

from csp import *


class NQueensTests(unittest.TestCase):

    @staticmethod
    def _n_queens_problem(n):
        """Creates a n-queens problem with variables and constraints.

        :param n: The dimension of the chessboard
        :type n: int
        :return: The n-queens problem
        """
        prob = Problem()

        # variables
        # one variable for each column, value is number of row
        d = list(range(1, n+1))
        for i in range(n):
            v = Variable(str(i+1), copy(d))
            prob.add_variable(v)

        # row constraints
        prob.add_constraint(AllDiff([v.name for v in prob.variables]))

        # diagonals constraint
        for i in range(n):
            for j in range(n):
                if i != j:
                    prob.add_constraint(DiffNotEqualValue(str(i+1), str(j+1), i - j))
                    prob.add_constraint(DiffNotEqualValue(str(j+1), str(i+1), i - j))

        return prob


    def test_2x2(self):
        prob = self._n_queens_problem(2)

        inf = ForwardChecking()
        var_sel = MinRemainingValues()
        solver = BacktrackSolver(inf, var_sel)

        solution = solver.solve(prob)
        self.assertEqual(solution, None)

    def test_8x8(self):
        prob = self._n_queens_problem(8)

        inf = ForwardChecking()
        var_sel = MinRemainingValues()
        solver = BacktrackSolver(inf, var_sel)

        solution = solver.solve(prob)
        pprint(solution)


if __name__ == '__main__':
    unittest.main()