import knapsack_solver_DP
import knapsack_solver_EA

def solve_dp(capacity, items):
    return knapsack_solver_DP.knapsack_dynamic_programming_solver(capacity, items)

def solve_ea(capacity, items):
    return knapsack_solver_EA.knapsack_evolutionary_solver(capacity, items)
