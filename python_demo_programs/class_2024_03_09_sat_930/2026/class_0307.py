M = int(input())

directions = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

x, y = 0, 0
visited = set()
visited.add((x, y))

count = 0

for _ in range(M):
    move = input()
    # S20
    d = move[0]
    steps = int(move[1:])

    dx, dy = directions[d]
    for _ in range(steps):
        x += dx
        y += dy

        if (x, y) in visited:
            count += 1

        visited.add((x, y))

print(count)
'''
3
S2
N2
S3
'''