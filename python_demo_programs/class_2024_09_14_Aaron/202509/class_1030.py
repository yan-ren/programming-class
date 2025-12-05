# 2024 J3
N = int(input())
score = []

for _ in range(N):
    score.append(int(input()))


first = 0
second = 0
third = 0
# [2, 2, 2, 2, 1]

# for value in score:
#     if value > first:
#         third = second
#         second = first
#         first = value
#     elif first > value > second:
#         third = second
#         second = value
#     elif second > value > third:
#         third = value

# remove duplicates
unique_score = []

for s in score:
    if s not in unique_score:
        unique_score.append(s)

# sorting
unique_score.sort()

# [3, 4, 5, 6, 7]
third = unique_score[len(unique_score) - 3]
# third = unique_score[-3]

# count = 0
# for value in score:
#     if value == third:
#         count += 1

count = score.count(third)
print(third, count)


