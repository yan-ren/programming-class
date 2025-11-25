C = int(input())

top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

total = 3 * (sum(top) + sum(bottom))

# subtract for horizontal adjacency in each row
for row in [top, bottom]:
    for i in range(C - 1):
        if row[i] == 1 and row[i] == row[i+1]:
            total -= 2

# subtract for vertical adjacency in column
for i in range(C):
    if top[i] == 1 and bottom[i] == 1 and (i % 2 == 0):
        total -= 2

print(total)