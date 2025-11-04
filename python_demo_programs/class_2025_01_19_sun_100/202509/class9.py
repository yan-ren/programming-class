# score = 90

# scores = [92, 89, 29, 100]
# # scores.sort()
# new_score = sorted(scores)
# print(scores)
# print(new_score)

# numbers = [2, 1, 3, 4, 2, 5]
# given a  list of numbers, find the largest / second largest

s = int(input())
scores = []

for _ in range(s):
    scores.append(int(input()))

# given a list of numbers, find the third largest value
# largest = -1
# second = -1
# third = -1
#
# for score in scores:
#     if score > largest:
#         third = second
#         second = largest
#         largest = score
#     elif largest > score > second:
#         third = second
#         second = score
#     elif second > score > third:
#         third = score

distinct_score = []
for score in scores:
    if score not in distinct_score:
        distinct_score.append(score)

distinct_score.sort()
# third = distinct_score[len(distinct_score)- 3]
third = distinct_score[-3]

count = scores.count(third)

print(third, count)


# 2023 J2
N = int(input())
shu = 0

for _ in range(N):
    pepper = input()
    if pepper == 'Poblano':
        shu += 1500