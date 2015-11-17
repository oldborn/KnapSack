"""A sample solver for the knapsack problem.

It takes each item randomly according to a probability."""

import random
import sys


def read_problem(file_name):
    lines = open(file_name).readlines()

    # get the number of items and total capacity
    tokens = lines[0].split()
    n_items = int(tokens[0])
    capacity = int(tokens[1])

    # collect the values and weights of each item
    items = []
    for line in lines[1 : n_items+1]:
        tokens = line.split()
        value = int(tokens[0])
        weight = int(tokens[1])
        item = (value, weight)
        items.append(item)

    # or:
    # n_items, capacity = map(int, lines[0].split())
    # items = [tuple(map(int, line.split())) for line in lines[1 : n_items+1]]
    return (capacity, items)


def solve(capacity, items, p=0.5):
    taken = []
    value = 0
    for item in items:
        # p: probability for taking an item
        if random.random() < p:
            taken.append(1)
            value += item[0]
        else:
            taken.append(0)

    # or:
    # taken = [(1 if random.random() < p else 0) for item in items]
    # value = sum([(v if t == 1 else 0) for (v, w), t in zip(items, taken)])
    return (taken, value)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s input_file" % sys.argv[0])
        sys.exit()

    file_name = sys.argv[1]
    capacity, items = read_problem(file_name)

    # to be deterministic, set a specific seed:
    # random.seed(799623108)

    taken, value = solve(capacity, items, p=0.4)

    print(value)
    print(taken[0], end='')
    for t in taken[1:]:
        print(' %d' % t, end='')
    print()
    # or:
    # print('%d\n%s' % (value, ' '.join(map(str, taken))))
