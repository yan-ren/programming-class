'''
2021 S1
'''
# N = int(input())
#
# heights = list(map(int, input().split()))
# widths = list(map(int, input().split()))
#
# total_twice_area = 0
#
# for i in range(N):
#     total_twice_area += (heights[i] + heights[i + 1]) * widths[i]
#
# if total_twice_area % 2 == 0:
#     print(total_twice_area // 2)
# else:
#     print(total_twice_area / 2)

M = int(input())
N = int(input())
K = int(input())

rows = [0] * M
cols = [0] * N

for _ in range(K):
    t, index = input().split()
    index = int(index) - 1

    if t == 'R':
        rows[index] += 1
    else:
        cols[index] += 1

# count odd flip
odd_rows = 0
for r in rows:
    if r % 2 == 1:
        odd_rows += 1

odd_cols = 0
for c in cols:
    if c % 2 == 1:
        odd_cols += 1

black = odd_rows * (N - odd_cols) + (M - odd_rows) * odd_cols
print(black)