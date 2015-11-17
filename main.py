import read
import solve

(capacity, items) = read.read_problem("data/ks_10000_0")
solution = solve.solve_dp(capacity, items)
print(solution)
