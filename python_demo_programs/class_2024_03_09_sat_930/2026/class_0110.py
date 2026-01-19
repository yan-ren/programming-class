'''
3 10 12 5
input() -> '3 10 12 5'
.split() -> ['3', '10, '12', '5']
map -> [3, 10, 12, 5]

'''

# d1, d2, d3, d4 = map(int, input().split())
#
# distance = [0, 0, 0, 0, 0]
# distance[0] = 0
# distance[1] = d1
# distance[2] = d1 + d2
# distance[3] = d1 + d2 + d3 # distance[2] + d3
# distance[4] = d1 + d2 + d3 + d4
#
# print(distance[0], distance[1], distance[2], distance[3], distance[4])
#
# for i in range(1, 5):
#     row = []
#     for j in range(5):
#         row.append(abs(distance[i] - distance[j]))
#     print(row[0], row[1], row[2], row[3], row[4])


# grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# rotate 90 degree clockwise
# grid = [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]

def rotate_90(grid):
    N = len(grid)
    new_grid = []

    for c in range(N):
        new_row = []
        for r in range(N):
            new_row.append(grid[N - 1 - r][c])

        new_grid.append(new_row)

    return new_grid

def check_increase(grid):
    for row in range(len(grid)):
        for col in range(len(grid) - 1):
            if grid[row][col] > grid[row][col+1]:
                return False

    for col in range(len(grid)):
        for row in range(len(grid) - 1):
            if grid[row][col] > grid[row+1][col]:
                return False

    return True


def print_result(grid):
    for row in grid:
        row = list(map(str, row))
        print(' '.join(row))

# print(rotate_90(grid))
N = int(input())
grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

for _ in range(4):
    grid = rotate_90(grid)
    if check_increase(grid):
        print_result(grid)
