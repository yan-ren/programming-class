'''
Problem J2: Fergusonball Ratings
'''
N = int(input())
stars = 0
for _ in range(N):
    score = int(input())
    foul = int(input())

    if score * 5 - foul * 3 > 40:
        stars += 1

if stars == N:
    print(str(stars) + "+")
else:
    print(stars)

