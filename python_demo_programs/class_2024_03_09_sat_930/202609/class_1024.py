'''
CCC 2026 j5

10
3
4
8 0
1 1
4 2
4
10
7
1
'''
N = int(input())
L = int(input())
Q = int(input())

illuminated = [0] * (N + 1)

for _ in range(L):
    P, S = map(int, input().split())
    left = max(1, P-S)
    right = min(N, P+S)
    for spot in range(left, right+1):
        illuminated[spot] += 1

answers = []
for _ in range(Q):
    spot = int(input())
    if illuminated[spot] > 0:
        answers.append('Y')
    else:
        answers.append('N')

print('\n'.join(answers))

# solution 2: prefix sum, 15/15
N = int(input())
L = int(input())
Q = int(input())

illuminated = [0] * (N + 2)

for _ in range(L):
    P, S = map(int, input().split())
    left = max(1, P-S)
    right = min(N, P+S)

    illuminated[left] += 1
    illuminated[right + 1] -= 1

for spot in range(1, N + 1):
    illuminated[spot] = illuminated[spot-1] + illuminated[spot]

answers = []
for _ in range(Q):
    spot = int(input())
    if illuminated[spot] > 0:
        answers.append('Y')
    else:
        answers.append('N')

print('\n'.join(answers))