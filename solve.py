import knapsack_solver_DP
import knapsack_solver_EA
import knapsack_solver_DP_Recursive


def solve_dp(capacity, items):
    return knapsack_solver_DP.knapsack_dynamic_programming_solver(capacity, items)

def solve_ea(capacity, items):
    return knapsack_solver_EA.knapsack_evolutionary_solver(capacity, items)

def solve_dp_recur(capacity, items):
    result_formatted = [0 for _ in range(len(items))]
    value, result = knapsack_solver_DP_Recursive.solve_dp_r(items, capacity)
    for r in result:
        result_formatted[r] = 1
    return value, result_formatted
