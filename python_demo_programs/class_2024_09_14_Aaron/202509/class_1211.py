'''
2024 J3
'''

# numbers = [70, 62, 58, 58, 73]

# sort a list
# numbers.sort(reverse=True)
# print(numbers)
# new_numbers = sorted(numbers, reverse=True)
# print(numbers)
# print(new_numbers)

# numbers = [1, 2, 1, 3, 2, 4]
# new_numbers = [1, 2, 3, 4]

'''
1. put all numbers into list
2. create a new list without duplicate
3. sort the deduplicated list and find third largest
4. in the original list find how many of third largest
# numbers = [1, 2, 1, 2, 4, 2, 3]
# print(numbers.count(2))
'''
# N = int(input())
# score = []
# for _ in range(N):
#     score.append(int(input()))

person = 'Y..Y.'
#
# count = [0, 0, 0, 0, 0]
#
# for i in range(len(person)):
#     if person[i] == 'Y':
#         count[i] += 1

# 2023 J3

# create a list as counter
# for each person, loop each day and count Y in counter
# find the largest in counter list
# find the position of the largest value

counter = [0, 0, 0, 0, 0]
N = int(input())
for _ in range(N):
    line = input() # 'YY.Y.'
    index = 0
    while index < len(line):
        if line[index] == 'Y':
            counter[index] += 1
        index += 1

# print(counter)
# [1, 2, 1, 3, 0]
most_people = max(counter)
days = []
index = 0
while index < len(counter):
    if counter[index] == most_people:
        days.append(str(index + 1))
    index += 1

# ['2', '5']
print(','.join(days))



