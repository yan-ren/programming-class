from queue import Queue

t = int(input())
for _ in range(t):
    row = int(input())
    col = int(input())
    maze = [list(input()) for _ in range(row)]
    seen = [[False] * col for _ in range(row)]
    step = [[0] * col for _ in range(row)]

    print(maze)
    print(seen)
    print(step)
    # BFS search of the maze
    seen[0][0] = True
    step[0][0] = 1
    q = Queue()
    q.put((0, 0))

    while not q.empty():
        r, c = q.get()
        # Go up if you can
        if ((maze[r][c] == '+' or maze[r][c] == '|') and r > 0 and maze[r - 1][c] != '*'
                and not seen[r - 1][c]):
            seen[r - 1][c] = True
            step[r - 1][c] = step[r][c] + 1
            q.put((r - 1, c))

        # Go down if you can
        if ((maze[r][c] == '+' or maze[r][c] == '|') and r < row - 1 and maze[r + 1][c] != '*'
                and not seen[r + 1][c]):
            seen[r + 1][c] = True
            step[r + 1][c] = step[r][c] + 1
            q.put((r + 1, c))

        # Go left if you can
        if ((maze[r][c] == '+' or maze[r][c] == '-') and c > 0 and maze[r][c - 1] != '*'
                and not seen[r][c - 1]):
            seen[r][c - 1] = True
            step[r][c - 1] = seen[r][c] + 1
            q.put((r, c - 1))

        # Go right if you can
        if ((maze[r][c] == '+' or maze[r][c] == '-') and c < col - 1
                and maze[r][c + 1] != '*' and not seen[r][c + 1]):
            seen[r][c + 1] = True
            step[r][c + 1] = step[r][c] + 1
            q.put((r, c + 1))

    if seen[row-1][col-1]:
        print(step[row - 1][col - 1])
    else:
        print(-1)