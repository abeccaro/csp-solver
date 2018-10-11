import unittest
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
        # one variable for each row, value is number of col
        d = [i + 1 for i in range(n)]
        vars = int_var_array(n, d)
        for v in vars:
            prob.add_variable(v)

        # row constraints
        prob.add_constraint(all_diff(vars))

        # diagonals constraint
        for i in range(n):
            for j in range(n):
                if i != j:
                    prob.add_constraint(arithmetic(vars[i], Operator.minus, vars[j], Operator.ne, i - j))
                    prob.add_constraint(arithmetic(vars[j], Operator.minus, vars[i], Operator.ne, i - j))

        return prob, vars


    def test_2x2(self):
        prob, vars = self._n_queens_problem(2)

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        self.assertEqual(solved, False)

        print('\n2 queens:\nNo solution')
        print(stats)

    def test_8x8(self):
        prob, vars = self._n_queens_problem(8)

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        self.assertEqual(solved, True)

        solution = [v.get_value() for v in vars]
        print('\n8 queens:')
        pprint(solution)
        print(stats)

    def test_20x20(self):
        prob, vars = self._n_queens_problem(20)

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        self.assertEqual(solved, True)

        solution = [v.get_value() for v in vars]
        print('\n20 queens:')
        pprint(solution)
        print(stats)

    def test_40x40(self):
        prob, vars = self._n_queens_problem(40)

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        self.assertEqual(solved, True)

        solution = [v.get_value() for v in vars]
        print('\n40 queens:')
        pprint(solution)
        print(stats)

    def test_60x60(self):
        prob, vars = self._n_queens_problem(60)

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        self.assertEqual(solved, True)

        solution = [v.get_value() for v in vars]
        print('\n60 queens:')
        pprint(solution)
        print(stats)

    def test_80x80(self):
        prob, vars = self._n_queens_problem(80)

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        self.assertEqual(solved, True)

        solution = [v.get_value() for v in vars]
        print('\n80 queens:')
        pprint(solution)
        print(stats)

    def test_100x100(self):
        prob, vars = self._n_queens_problem(100)

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        self.assertEqual(solved, True)

        solution = [v.get_value() for v in vars]
        print('\n100 queens:')
        pprint(solution)
        print(stats)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(NQueensTests('test_2x2'))
    suite.addTest(NQueensTests('test_8x8'))
    suite.addTest(NQueensTests('test_20x20'))
    suite.addTest(NQueensTests('test_40x40'))
    suite.addTest(NQueensTests('test_60x60'))
    suite.addTest(NQueensTests('test_80x80'))
    suite.addTest(NQueensTests('test_100x100'))

    unittest.TextTestRunner().run(suite)
