def delete_greatest_value(grid):
    # sort each row in the grid
    for i in range(len(grid)):
        grid[i].sort()

    col_number = len(grid[0])
    result = 0
    while col_number > 0:
        deleted_nums = []
        # loop through each row
        for i in range(len(grid)):
            deleted_nums.append(grid[i][col_number - 1])

        result += max(deleted_nums)
        col_number -= 1

    return result


print(delete_greatest_value([[1, 2, 4], [3, 3, 1]]))
