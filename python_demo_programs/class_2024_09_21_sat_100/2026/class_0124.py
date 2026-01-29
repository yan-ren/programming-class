def min_wall_perimeter(A, B, X, Y):
    # place paints side by side horizontally
    width1 = A + X
    height1 = max(B, Y)
    perimeter1 = 2 * (width1 + height1)

    # stack paintings vertically
    width2 = max(A, X)
    height2 = B + Y
    perimeter2 = 2 * (width2 + height2)

    return min(perimeter1, perimeter2)

A, B, X, Y = map(int, input().split())
print(min_wall_perimeter(A, B, X, Y))


# 2024 S1
N = int(input())
hats = [int(input()) for _ in range(N)]

half = N//2
count = 0
for i in range(N):
    j = (i + half) % N
    if hats[i] == hats[j]:
        count += 1

print(count)

