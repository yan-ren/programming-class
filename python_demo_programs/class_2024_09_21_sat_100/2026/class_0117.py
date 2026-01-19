def rotate_90(grid):
    N = len(grid)
    new_grid = []

    for col in range(N):
        new_row = []
        for row in range(N):
            new_row.append(grid[N - 1 - row][col])
        new_grid.append(new_row)

    return new_grid

def is_valid_sunflower(grid):
    N = len(grid)
    for r in range(N):
        for c in range(N - 1):
            if grid[r][c] >= grid[r][c + 1]:
                return False
    for c in range(N):
        for r in range(N - 1):
            if grid[r][c] >= grid[r + 1][c]:
                return False

    return True


N = int(input())
grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))

for _ in range(4):
    if is_valid_sunflower(grid):
        for row in grid:
            print(' '.join(map(str, row)))
        break
    grid = rotate_90(grid)