def knapsack_dynamic_programming_solver(capacity, items):
    # memoization_matrix = [[0 for x in range(items.__len__())] for x in range(capacity)]
    matrix = []
    matrix.append([0 for x in range(capacity + 1)])
    for i in range(1, items.__len__()+1):
        matrix.append([0] + [-1 for x in range(1, capacity + 1)])
    for i in range(1, items.__len__()+1):
        for w in range(capacity + 1):
            if items[i - 1][1] <= w:
                if items[i - 1][0] + matrix[i - 1][w - items[i - 1][1]] > matrix[i - 1][w]:
                    matrix[i][w] = items[i - 1][0] + matrix[i - 1][w - items[i - 1][1]]
                else:
                    matrix[i][w] = matrix[i - 1][w]
            else:
                matrix[i][w] = matrix[i - 1][w]
    return matrix[items.__len__()][capacity]
