# l = [[1, 2], [2, 10, 3]]
#
# for a in l:
#     for v in a:
#         print(v)
#
#
# result = [2, 10]

import turtle

grid = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

CELL_SIZE = 40
ROWS = len(grid)
COLS = len(grid[0])

turtle.speed(0)
turtle.penup()

for row in range(ROWS):
    for col in range(COLS):
        x = col * CELL_SIZE - (COLS * CELL_SIZE) // 2
        y = (ROWS * CELL_SIZE) // 2 - row * CELL_SIZE
        turtle.goto(x, y)

        if grid[row][col] == 1:
            turtle.color("black")
        else:
            turtle.color("white")

        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(CELL_SIZE)
            turtle.right(90)
        turtle.end_fill()

turtle.done()
