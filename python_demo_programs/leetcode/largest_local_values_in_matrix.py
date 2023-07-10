def largest_local(grid):
    # create output 2d list
    n = len(grid)
    result = [[0 for j in range(n-2)] for i in range(n-2)]

    for row in range(n - 2):
        for col in range(n - 2):
            # find the largest in 3x3 matrix
            for inner_row in range(row, row + 3):
                for inner_col in range(col, col + 3):
                    result[inner_row][inner_col] = max(result[inner_row][inner_col], grid[inner_row][inner_col])

    return result