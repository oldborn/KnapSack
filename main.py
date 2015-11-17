import read
import solve
import sys

if len(sys.argv) != 2:
        print("Usage: %s input_file" % sys.argv[0])
        sys.exit()

#(capacity, items) = read.read_problem("data/ks_19_0")
capacity, items = read.read_problem(sys.argv[1])
value, taken = solve.solve_dp(capacity, items)

print('%d\n%s' % (value, ' '.join(map(str, taken))))
