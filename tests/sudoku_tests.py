import unittest
from math import sqrt

from csp import *


class SudokuTests(unittest.TestCase):

    @staticmethod
    def _sudoku_problem(hints):
        """Creates a problem that represents a sudoku.
        
        'hints' matrix is assumed square, no hint is represented with 0.

        :param hints: The matrix of initial hints
        :type hints: list
        :return: The empty sudoku problem
        """
        prob = Problem()
        dim = len(hints)

        # variables
        d = [i + 1 for i in range(dim)]
        vars = int_var_matrix(dim, dim, d, name='x')
        for row in vars:
            for v in row:
                prob.add_variable(v)

        # rows and cols constraints
        for i in range(dim):
            col_vars = []
            for j in range(dim):
                col_vars.append(vars[j][i])
            prob.add_constraint(all_diff(vars[i], 'row' + str(i + 1)))
            prob.add_constraint(all_diff(col_vars, 'col' + str(i + 1)))

        # squares constraints
        root = int(sqrt(dim))
        for i in range(0, dim, root):
            for j in range(0, dim, root):
                square_vars = []
                for k in range(root):
                    for l in range(root):
                        square_vars.append(vars[i + k][j + l])
                prob.add_constraint(all_diff(square_vars, 'square' + str(i + 1) + str(j + 1)))

        # initial hints
        for i in range(dim):
            for j in range(dim):
                if hints[i][j] != 0:
                    prob.add_constraint(arithmetic(vars[i][j], Operator.eq, hints[i][j],
                                                   name='hint' + str(i + 1) + str(j + 1)))

        return prob, vars

    # Easy
    def test_sudoku_1(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [0, 5, 2, 6, 0, 0, 4, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 9, 0, 7, 8, 3, 0, 6, 2],
            [0, 0, 5, 0, 4, 0, 8, 0, 9],
            [0, 0, 6, 0, 0, 0, 7, 0, 0],
            [2, 0, 3, 0, 7, 0, 1, 0, 0],
            [1, 2, 0, 5, 3, 9, 0, 7, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 7, 9, 0, 0, 8, 3, 5, 0]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)
        solution = [[v.get_value() for v in row] for row in vars]

        expected = [
            [3, 5, 2, 6, 9, 1, 4, 8, 7],
            [8, 6, 7, 2, 5, 4, 9, 1, 3],
            [4, 9, 1, 7, 8, 3, 5, 6, 2],
            [7, 1, 5, 3, 4, 6, 8, 2, 9],
            [9, 4, 6, 8, 1, 2, 7, 3, 5],
            [2, 8, 3, 9, 7, 5, 1, 4, 6],
            [1, 2, 8, 5, 3, 9, 6, 7, 4],
            [5, 3, 4, 1, 6, 7, 2, 9, 8],
            [6, 7, 9, 4, 2, 8, 3, 5, 1]
        ]

        self.assertEqual(solution, expected)
        print(stats)

    # Hard
    def test_sudoku_2(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [0, 0, 1, 0, 0, 0, 0, 0, 9],
            [0, 0, 5, 0, 7, 9, 0, 2, 0],
            [7, 9, 0, 0, 0, 3, 8, 0, 0],
            [0, 0, 0, 0, 1, 0, 3, 9, 0],
            [0, 2, 0, 3, 0, 8, 0, 4, 0],
            [0, 7, 8, 0, 6, 0, 0, 0, 0],
            [0, 0, 7, 5, 0, 0, 0, 6, 4],
            [0, 5, 0, 8, 9, 0, 7, 0, 0],
            [9, 0, 0, 0, 0, 0, 5, 0, 0]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)
        solution = [[v.get_value() for v in row] for row in vars]

        expected = [
            [2, 3, 1, 6, 8, 5, 4, 7, 9],
            [6, 8, 5, 4, 7, 9, 1, 2, 3],
            [7, 9, 4, 1, 2, 3, 8, 5, 6],
            [5, 4, 6, 2, 1, 7, 3, 9, 8],
            [1, 2, 9, 3, 5, 8, 6, 4, 7],
            [3, 7, 8, 9, 6, 4, 2, 1, 5],
            [8, 1, 7, 5, 3, 2, 9, 6, 4],
            [4, 5, 2, 8, 9, 6, 7, 3, 1],
            [9, 6, 3, 7, 4, 1, 5, 8, 2]
        ]

        self.assertEqual(solution, expected)
        print(stats)

    # Hard
    def test_sudoku_3(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [5, 6, 0, 0, 0, 8, 0, 1, 0],
            [2, 3, 0, 4, 0, 0, 0, 0, 8],
            [0, 0, 0, 1, 3, 0, 2, 0, 0],
            [0, 4, 3, 5, 0, 0, 0, 0, 6],
            [0, 0, 2, 0, 0, 0, 5, 0, 0],
            [6, 0, 0, 0, 0, 2, 8, 4, 0],
            [0, 0, 4, 0, 1, 3, 0, 0, 0],
            [3, 0, 0, 0, 0, 4, 0, 9, 2],
            [0, 8, 0, 9, 0, 0, 0, 7, 3]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)
        solution = [[v.get_value() for v in row] for row in vars]

        expected = [
            [5, 6, 9, 2, 7, 8, 3, 1, 4],
            [2, 3, 1, 4, 5, 9, 7, 6, 8],
            [4, 7, 8, 1, 3, 6, 2, 5, 9],
            [7, 4, 3, 5, 8, 1, 9, 2, 6],
            [8, 9, 2, 6, 4, 7, 5, 3, 1],
            [6, 1, 5, 3, 9, 2, 8, 4, 7],
            [9, 2, 4, 7, 1, 3, 6, 8, 5],
            [3, 5, 7, 8, 6, 4, 1, 9, 2],
            [1, 8, 6, 9, 2, 5, 4, 7, 3]
        ]

        self.assertEqual(solution, expected)
        print(stats)


if __name__ == '__main__':
    unittest.main()
