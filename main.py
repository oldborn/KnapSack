import read
import solve

(capacity, items) = read.read_problem("data/ks_500_0")
solve.solve_dp(capacity, items)
