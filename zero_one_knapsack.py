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


def solve_dynamic_prog(weights, profits, weight_limit):
    current_best_knapsacks = [None] * (weight_limit + 1)
    current_best_profits = [0] * (weight_limit + 1)
    # Iterate through each item.
    for item_idx, item_weight in enumerate(weights):
        profit = profits[item_idx]
        new_best_knapsacks = current_best_knapsacks[:item_weight]
        new_best_profits = current_best_profits[:item_weight]
        # Iterate through each smaller knapsack weight.
        for knapsack_weight in range(item_weight, weight_limit + 1):
            new_profit_with_item = current_best_profits[knapsack_weight - item_weight] + profit
            current_profit_without_item = current_best_profits[knapsack_weight]
            if new_profit_with_item > current_profit_without_item:
                try:
                    current_knapsack = current_best_knapsacks[knapsack_weight -
                                                            item_weight][:]
                    current_knapsack.append(item_idx)
                    new_best_knapsacks.append(current_knapsack)
                except:
                    new_best_knapsacks.append([item_idx])
                new_best_profits.append(new_profit_with_item)
            else:
                new_best_knapsacks.append(current_best_knapsacks[knapsack_weight])
                new_best_profits.append(current_profit_without_item)
        current_best_knapsacks = new_best_knapsacks
        current_best_profits = new_best_profits
    return current_best_knapsacks[-1]

def solve_bandb_same_values(weights_list, weight_limit):
    """Every item in the list has the same value per weight unit."""
    items_set = [WeightProfitTuple(weight=w, profit=w) for w in weights_list]
    solver = Solver(items_set, weight_limit)
    # Best fitting weights
    solver.solve_branch_and_bound()
    return [item.weight for item in solver.solution]

