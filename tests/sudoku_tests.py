import unittest
from copy import copy

from csp import *


class SudokuTests(unittest.TestCase):

    @staticmethod
    def __sudoku_problem():
        prob = Problem()

        # variables
        d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            for j in range(9):
                vij = Variable(str(i + 1) + ',' + str(j + 1), copy(d))
                prob.add_variable(vij)

        # rows and cols constraints
        for i in range(9):
            row_vars = []
            col_vars = []
            for j in range(9):
                row_vars.append(str(i + 1) + ',' + str(j + 1))
                col_vars.append(str(j + 1) + ',' + str(i + 1))
            prob.add_constraint(AllDiff(row_vars))
            prob.add_constraint(AllDiff(col_vars))

        # squares constraints
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                square_vars = []
                for k in range(3):
                    for l in range(3):
                        square_vars.append(str(i + k) + ',' + str(j + l))
                prob.add_constraint(AllDiff(square_vars))

        return prob

    @staticmethod
    def __sudoku_hints(prob, matrix):
        for i in range(9):
            for j in range(9):
                if matrix[i][j] != 0:
                    prob.add_constraint(EqualsValue(str(i+1) + ',' + str(j+1), matrix[i][j]))

    @staticmethod
    def __sudoku_solution(matrix):
        sol = {}
        for i in range(9):
            for j in range(9):
                sol[str(i+1) + ',' + str(j+1)] = matrix[i][j]
        return sol


    def test_sudoku_1(self):
        # base sudoku problem
        prob = SudokuTests.__sudoku_problem()

        # adding initial hints
        self.__sudoku_hints(prob, [
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


        # solver setup
        inf = ForwardChecking()
        var_sel = MinRemainingValues()
        solver = BacktrackSolver(inf, var_sel)

        #calculating solution
        solution = solver.solve(prob)

        expected = self.__sudoku_solution([
            [3, 5, 2, 6, 9, 1, 4, 8, 7],
            [8, 6, 7, 2, 5, 4, 9, 1, 3],
            [4, 9, 1, 7, 8, 3, 5, 6, 2],
            [7, 1, 5, 3, 4, 6, 8, 2, 9],
            [9, 4, 6, 8, 1, 2, 7, 3, 5],
            [2, 8, 3, 9, 7, 5, 1, 4, 6],
            [1, 2, 8, 5, 3, 9, 6, 7, 4],
            [5, 3, 4, 1, 6, 7, 2, 9, 8],
            [6, 7, 9, 4, 2, 8, 3, 5, 1]
        ])
        self.assertEqual(solution.assignments, expected)


    def test_sudoku_2(self):
        # base sudoku problem
        prob = SudokuTests.__sudoku_problem()

        # adding initial hints
        self.__sudoku_hints(prob, [
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


        # solver setup
        inf = ForwardChecking()
        var_sel = MinRemainingValues()
        solver = BacktrackSolver(inf, var_sel)

        #calculating solution
        solution = solver.solve(prob)


        expected = self.__sudoku_solution([
            [2, 3, 1, 6, 8, 5, 4, 7, 9],
            [6, 8, 5, 4, 7, 9, 1, 2, 3],
            [7, 9, 4, 1, 2, 3, 8, 5, 6],
            [5, 4, 6, 2, 1, 7, 3, 9, 8],
            [1, 2, 9, 3, 5, 8, 6, 4, 7],
            [3, 7, 8, 9, 6, 4, 2, 1, 5],
            [8, 1, 7, 5, 3, 2, 9, 6, 4],
            [4, 5, 2, 8, 9, 6, 7, 3, 1],
            [9, 6, 3, 7, 4, 1, 5, 8, 2]
        ])
        self.assertEqual(solution.assignments, expected)


if __name__ == '__main__':
    unittest.main()