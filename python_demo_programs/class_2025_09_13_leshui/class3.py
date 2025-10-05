'''
Given a list number, find how many positive values and how many negative values

'''
numbers = [1, 2, -1, 3]
positive = 0
negative = 0

for value in numbers:
    if value > 0:
        positive += 1
    if value < 0:
        negative += 1

print(positive, negative)

'''
how to generate a list: [1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
l = []

for i in range(1, 10):
    l.append(i * i)


'''
given a list numbers, some numbers are duplicated, how to create a new list without duplicates

e.g.
given [1, 2, 1, 4, 2, 5]
create [1, 2, 4, 5]
'''
# numbers = [1, 2, 1, 4, 2, 5]
# new_numbers = []
#
# for value in numbers:
#     if value not in new_numbers:
#         new_numbers.append(value)
#
# print(new_numbers)


# i = 0
# while i < len(numbers):
#     if numbers.count(numbers[i]) > 1:
#         del numbers[i]
#     else:
#         i += 1

'''
given a list numbers, some numbers are negative, how to create a new list without negative

e.g.
given [1, 2, 1, -4, -2, 5]
create [1, 2, 1, 5]
'''

