# see http://www.jstor.org/stable/10.2307/2634886
from collections import namedtuple

WeightProfitTuple = namedtuple('WeightProfitTuple', 'weight profit')

class Solver:
    """Constructor accepts a list of candidates in the form of (weight,
    profit) tuples. The solve_branch_and_bound() method finds a solution, and the resulting
    optimal candidate set can be accessed via the solution set attribute.
    """

    def __init__(self, candidates, limit):
        self.candidates = candidates
        self.limit = limit
        self._current_best_solution = []
        self._current_best_profit = 0

    def solve_branch_and_bound(self):
        current_weight = 0
        current_profit = 0
        so_far = []
        remaining = self.candidates
        # Start the recursive branching and bounding
        self.branch(current_weight, current_profit, so_far, remaining)
        # Save the best solution found.
        self.solution = self._current_best_solution

    def branch(self, current_weight, current_profit, items_so_far,
               items_remaining):
        if current_weight > self.limit:
            # Too much weight. Don't branch further.
            return
        if current_profit > self._current_best_profit:
            # Found a new best profit.
            self._current_best_profit = current_profit
            self._current_best_solution = items_so_far
        for idx, next_candt in enumerate(items_remaining):
            next_total_weight = current_weight + next_candt.weight
            next_total_profit = current_profit + next_candt.profit
            items_so_far_next_level = items_so_far[:]
            items_so_far_next_level.append(next_candt)
            items_remaining_next_level = items_remaining[:]
            del items_remaining_next_level[idx]
            self.branch(next_total_weight, next_total_profit,
                        items_so_far_next_level, items_remaining_next_level)


def solve_same_values(weights_list, weight_limit):
    """Every item in the list has the same value per weight unit."""
    items_set = [WeightProfitTuple(weight=w, profit=w) for w in weights_list]
    solver = Solver(items_set, weight_limit)
    # Best fitting weights
    solver.solve_branch_and_bound()
    return [item.weight for item in solver.solution]


################
#  Unit tests  #
################

import unittest
class TestZeroOneKnapsack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #cls.rows = read_csv()
        pass

    def setUp(self):
        self.ex357_equ_wt_candts = [WeightProfitTuple(3,3),
                                    WeightProfitTuple(5,5),
                                    WeightProfitTuple(7,7)]

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
