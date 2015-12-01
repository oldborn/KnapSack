import memoize

def solve_dp_r(items, maxweight):
    @memoize.memoized
    def bestvalue(i, j):
        if i == 0:
            return 0
        value, weight = items[i - 1]
        if weight > j:
            return bestvalue(i - 1, j)
        else:
            return max(bestvalue(i - 1, j),
                       bestvalue(i - 1, j - weight) + value)

    j = maxweight
    result = []
    for i in range(len(items), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            result.append(i - 1)
            j -= items[i - 1][1]
    result.reverse()
    return bestvalue(len(items), maxweight), result