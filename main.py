import read
import solve
import sys

# if len(sys.argv) != 2:
#         print("Usage: %s input_file" % sys.argv[0])
#         sys.exit()
sys.setrecursionlimit(100000)
(capacity, items) = read.read_problem("data/ks_200_1")
# capacity, items = read.read_problem(sys.argv[1])
value, taken = solve.solve_dp_recur(capacity, items)
print('%d\n%s' % (value, ' '.join(map(str, taken))))
