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
        vars = []
        for row in range(dim):
            vars.append([])
            for col in range(dim):
                v = int_var(
                    d if hints[row][col] == 0 else [hints[row][col]],
                    name='x' + str(row + 1) + str(col + 1))
                prob.add_variable(v)
                vars[row].append(v)


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

        return prob, vars


    def test_easy_a(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [0, 0, 2, 0, 0, 0, 5, 0, 0],
            [0, 1, 0, 7, 0, 5, 0, 2, 0],
            [4, 0, 0, 0, 9, 0, 0, 0, 7],
            [0, 4, 9, 0, 0, 0, 7, 3, 0],
            [8, 0, 1, 0, 3, 0, 4, 0, 9],
            [0, 3, 6, 0, 0, 0, 2, 1, 0],
            [2, 0, 0, 0, 8, 0, 0, 0, 4],
            [0, 8, 0, 9, 0, 2, 0, 6, 0],
            [0, 0, 7, 0, 0, 0, 8, 0, 0]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        # solution = [[v.get_value() for v in row] for row in vars]
        # print(solution)

        print(stats)

    def test_easy_b(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [0, 5, 0, 0, 1, 0, 0, 4, 0],
            [1, 0, 7, 0, 0, 0, 6, 0, 2],
            [0, 0, 0, 9, 0, 5, 0, 0, 0],
            [2, 0, 8, 0, 3, 0, 5, 0, 1],
            [0, 4, 0, 0, 7, 0, 0, 2, 0],
            [9, 0, 1, 0, 8, 0, 4, 0, 6],
            [0, 0, 0, 4, 0, 1, 0, 0, 0],
            [3, 0, 4, 0, 0, 0, 7, 0, 9],
            [0, 2, 0, 0, 6, 0, 0, 1, 0]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        # solution = [[v.get_value() for v in row] for row in vars]
        # print(solution)

        print(stats)

    def test_easy_c(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [0, 0, 0, 6, 0, 2, 0, 0, 0],
            [4, 0, 0, 0, 5, 0, 0, 0, 1],
            [0, 8, 5, 0, 1, 0, 6, 2, 0],
            [0, 3, 8, 2, 0, 6, 7, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 9, 4, 0, 7, 3, 5, 0],
            [0, 2, 6, 0, 4, 0, 5, 3, 0],
            [9, 0, 0, 0, 2, 0, 0, 0, 7],
            [0, 0, 0, 8, 0, 9, 0, 0, 0]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        # solution = [[v.get_value() for v in row] for row in vars]
        # print(solution)

        print(stats)

    def test_medium_a(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 7, 9, 0, 5, 0, 1, 8, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 7, 3, 0, 6, 8, 0, 0],
            [4, 5, 0, 7, 0, 8, 0, 9, 6],
            [0, 0, 3, 5, 0, 2, 7, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 5],
            [0, 1, 6, 0, 3, 0, 4, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        # solution = [[v.get_value() for v in row] for row in vars]
        # print(solution)

        print(stats)

    def test_medium_b(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [0, 0, 0, 0, 0, 0, 0, 8, 5],
            [0, 0, 0, 2, 1, 0, 0, 0, 9],
            [9, 6, 0, 0, 8, 0, 1, 0, 0],
            [5, 0, 0, 8, 0, 0, 0, 1, 6],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [8, 9, 0, 0, 0, 6, 0, 0, 7],
            [0, 0, 9, 0, 7, 0, 0, 5, 2],
            [3, 0, 0, 0, 5, 4, 0, 0, 0],
            [4, 8, 0, 0, 0, 0, 0, 0, 0]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        # solution = [[v.get_value() for v in row] for row in vars]
        # print(solution)

        print(stats)

    def test_medium_c(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [7, 0, 0, 0, 0, 4, 0, 0, 1],
            [0, 2, 0, 0, 6, 0, 0, 8, 0],
            [0, 0, 1, 5, 0, 0, 2, 0, 0],
            [8, 0, 0, 0, 9, 0, 7, 0, 0],
            [0, 5, 0, 3, 0, 7, 0, 2, 0],
            [0, 0, 6, 0, 5, 0, 0, 0, 8],
            [0, 0, 8, 0, 0, 9, 1, 0, 0],
            [0, 9, 0, 0, 1, 0, 0, 6, 0],
            [5, 0, 0, 8, 0, 0, 0, 0, 3]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        # solution = [[v.get_value() for v in row] for row in vars]
        # print(solution)

        print(stats)

    def test_hard_a(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [0, 0, 0, 0, 0, 3, 0, 1, 7],
            [0, 1, 5, 0, 0, 9, 0, 0, 8],
            [0, 6, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 5, 0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 0, 2, 0],
            [5, 0, 0, 6, 0, 0, 3, 4, 0],
            [3, 4, 0, 2, 0, 0, 0, 0, 0]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        # solution = [[v.get_value() for v in row] for row in vars]
        # print(solution)

        print(stats)

    def test_hard_b(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [3, 8, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 7, 8, 5],
            [0, 0, 9, 0, 2, 0, 3, 0, 0],
            [0, 6, 0, 0, 9, 0, 0, 0, 0],
            [8, 0, 0, 3, 0, 2, 0, 0, 9],
            [0, 0, 0, 0, 4, 0, 0, 7, 0],
            [0, 0, 1, 0, 7, 0, 5, 0, 0],
            [4, 9, 5, 0, 0, 6, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 9, 2]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        # solution = [[v.get_value() for v in row] for row in vars]
        # print(solution)

        print(stats)

    def test_hard_c(self):
        # base sudoku problem
        prob, vars = SudokuTests._sudoku_problem([
            [0, 0, 0, 7, 0, 0, 8, 0, 0],
            [0, 0, 6, 0, 0, 0, 0, 3, 1],
            [0, 4, 0, 0, 0, 2, 0, 0, 0],
            [0, 2, 4, 0, 7, 0, 0, 0, 0],
            [0, 1, 0, 0, 3, 0, 0, 8, 0],
            [0, 0, 0, 0, 6, 0, 2, 9, 0],
            [0, 0, 0, 8, 0, 0, 0, 7, 0],
            [8, 6, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 2, 0, 0, 6, 0, 0, 0]
        ])

        solver = BacktrackSolver()

        solved, stats = solver.solve(prob)

        # solution = [[v.get_value() for v in row] for row in vars]
        # print(solution)

        print(stats)


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(SudokuTests('test_easy_a'))
    suite.addTest(SudokuTests('test_easy_b'))
    suite.addTest(SudokuTests('test_easy_c'))

    suite.addTest(SudokuTests('test_medium_a'))
    suite.addTest(SudokuTests('test_medium_b'))
    suite.addTest(SudokuTests('test_medium_c'))

    suite.addTest(SudokuTests('test_hard_a'))
    suite.addTest(SudokuTests('test_hard_b'))
    suite.addTest(SudokuTests('test_hard_c'))

    unittest.TextTestRunner().run(suite)
