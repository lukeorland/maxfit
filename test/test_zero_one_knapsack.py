import unittest
from zero_one_knapsack import WeightProfitTuple, Solver, solve_dynamic_prog

class TestZeroOneKnapsack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #cls.rows = read_csv()
        pass

    def setUp(self):
        self.ex357_equ_wt_candts = [WeightProfitTuple(3,3),
                                    WeightProfitTuple(5,5),
                                    WeightProfitTuple(7,7)]
        self.weights = [2, 3, 4, 5]
        self.profits = [3, 4, 5, 6]
        self.limit = 5

    def test_Solver(self):
        assert Solver(self.ex357_equ_wt_candts, 10) is not None

    def test_Solver_solution_ex357_10(self):
        solver = Solver(self.ex357_equ_wt_candts, 10)
        solver.solve_branch_and_bound()
        expected = set([WeightProfitTuple(3,3), WeightProfitTuple(7,7)])
        actual = set(solver.solution)
        #actual = set(solver._current_best_solution)
        self.assertEqual(expected, actual)

    def test_Solver_empty_solution(self):
        solver = Solver(self.ex357_equ_wt_candts, 2)
        solver.solve_branch_and_bound()
        expected = []
        actual = solver.solution
        self.assertEqual(expected, actual)

    def test_Solver_branch_10_1(self):
        solver = Solver(self.ex357_equ_wt_candts, 10)
        solver._current_best_solution = [WeightProfitTuple(3,3),
                                        WeightProfitTuple(5,5)]
        total_weight_so_far = 8
        total_profit_so_far = 8
        items_so_far = [WeightProfitTuple(3,3),
                        WeightProfitTuple(5,5)]
        remaining_candidates = [WeightProfitTuple(7,7)]
        solver.branch(total_weight_so_far, total_profit_so_far, items_so_far,
                      remaining_candidates)
        # The current best solution should not have been updated.
        expected = set([WeightProfitTuple(3,3), WeightProfitTuple(5,5)])
        actual = set(solver._current_best_solution)
        self.assertEqual(expected, actual)

    def test_Solver_branch_10_2(self):
        solver = Solver(self.ex357_equ_wt_candts, 10)
        solver._current_best_solution = [WeightProfitTuple(3,3),
                                        WeightProfitTuple(7,7)]
        total_weight_so_far = 10
        total_profit_so_far = 10
        items_so_far = [WeightProfitTuple(3,3),
                        WeightProfitTuple(7,7)]
        remaining_candidates = [WeightProfitTuple(5,5)]
        solver.branch(total_weight_so_far, total_profit_so_far, items_so_far,
                      remaining_candidates)
        # The current best solution should not have been updated.
        expected = set([WeightProfitTuple(3,3), WeightProfitTuple(7,7)])
        actual = set(solver._current_best_solution)
        self.assertEqual(expected, actual)

    def test_Solver_branch_10_3(self):
        solver = Solver(self.ex357_equ_wt_candts, 10)
        solver._current_best_solution = [WeightProfitTuple(7,7)]
        total_weight_so_far = 10
        total_profit_so_far = 10
        items_so_far = [WeightProfitTuple(7,7)]
        remaining_candidates = [WeightProfitTuple(5,5)]
        solver.branch(total_weight_so_far, total_profit_so_far, items_so_far,
                      remaining_candidates)
        # The current best solution should not have been updated.
        expected = set([WeightProfitTuple(7,7)])
        actual = set(solver._current_best_solution)
        self.assertEqual(expected, actual)

    def test_Solver_branch_10_4(self):
        solver = Solver(self.ex357_equ_wt_candts, 10)
        solver._current_best_solution = [WeightProfitTuple(3,3)]
        total_weight_so_far = 3
        total_profit_so_far = 3
        items_so_far = [WeightProfitTuple(3,3)]
        remaining_candidates = [WeightProfitTuple(7,7)]
        solver.branch(total_weight_so_far, total_profit_so_far, items_so_far,
                      remaining_candidates)
        # The current best solution should not have been updated.
        expected = set([WeightProfitTuple(3,3), WeightProfitTuple(7,7)])
        actual = set(solver._current_best_solution)
        self.assertEqual(expected, actual)

    def test_Solver_branch_10_5(self):
        solver = Solver(self.ex357_equ_wt_candts, 10)
        solver._current_best_solution = [WeightProfitTuple(7,7)]
        total_weight_so_far = 10
        total_profit_so_far = 10
        items_so_far = [WeightProfitTuple(7,7)]
        remaining_candidates = [WeightProfitTuple(5,5)]
        solver.branch(total_weight_so_far, total_profit_so_far, items_so_far,
                      remaining_candidates)
        # The current best solution should not have been updated.
        expected = set([WeightProfitTuple(7,7)])
        actual = set(solver._current_best_solution)
        self.assertEqual(expected, actual)

    def test_Solver_branch_11(self):
        new_candidates = [WeightProfitTuple(5,5),
                          WeightProfitTuple(3,3),
                          WeightProfitTuple(7,7)]
        solver = Solver(new_candidates, 11)
        solver.solve_branch_and_bound()
        # The current best solution should have been updated.
        expected = set([WeightProfitTuple(3,3),
                        WeightProfitTuple(7,7)])
        actual = set(solver._current_best_solution)
        self.assertEqual(expected, actual)

    def test_Solver_branch_15_1(self):
        solver = Solver(self.ex357_equ_wt_candts, 15)
        solver._current_best_solution = [WeightProfitTuple(3,3),
                                        WeightProfitTuple(5,5)]
        total_weight_so_far = 8
        total_profit_so_far = 8
        items_so_far = [WeightProfitTuple(3,3),
                  WeightProfitTuple(5,5)]
        remaining_candidates = [WeightProfitTuple(7,7)]
        solver.branch(total_weight_so_far, total_profit_so_far, items_so_far,
                      remaining_candidates)
        # The current best solution should have been updated.
        expected = set([WeightProfitTuple(3,3), WeightProfitTuple(5,5),
                        WeightProfitTuple(7,7)])
        actual = set(solver._current_best_solution)
        self.assertEqual(expected, actual)

    def test_Solver_branch_13(self):
        new_candidates = [WeightProfitTuple(5,5),
                          WeightProfitTuple(3,3),
                          WeightProfitTuple(7,7)]
        solver = Solver(new_candidates, 13)
        solver.solve_branch_and_bound()
        # The current best solution should have been updated.
        expected = set([WeightProfitTuple(5,5),
                        WeightProfitTuple(7,7)])
        actual = set(solver._current_best_solution)
        self.assertEqual(expected, actual)

    def test_Solver_branch_13_1(self):
        solver = Solver(self.ex357_equ_wt_candts, 13)
        solver._current_best_solution = [WeightProfitTuple(7,7),
                                        WeightProfitTuple(3,3)]
        total_weight_so_far = 10
        total_profit_so_far = 10
        items_so_far = [WeightProfitTuple(3,3),
                  WeightProfitTuple(7,7)]
        remaining_candidates = [WeightProfitTuple(5,5)]
        solver.branch(total_weight_so_far, total_profit_so_far, items_so_far,
                      remaining_candidates)
        # The current best solution should not have been updated.
        expected = set([WeightProfitTuple(3,3),
                        WeightProfitTuple(7,7)])
        actual = set(solver._current_best_solution)
        self.assertEqual(expected, actual)

    def test_solve_dyn_prog(self):
        self.assertEqual([0, 1], solve_dynamic_prog(self.weights,
                                                    self.profits,
                                                    self.limit))

