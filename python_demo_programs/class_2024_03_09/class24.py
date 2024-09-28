# D = int(input())
#
# while True:
#     Y = int(input())
#     if Y >= D:
#         break
#
#     D += Y
#
# print(D)

# comprehension
numbers = [2, 1, -4, 2, -5, 6]
# new_numbers = []
#
# for num in numbers:
#     if num > 0:
#         new_numbers.append(num)

# new_numbers = [num for num in numbers if num > 0]

# convert following program to comprehension
numbers = [1, 2, 3, 4, -1]
new_numbers = []
for num in numbers:
    new_numbers.append(num * -1)


new_numbers = [num * -1 for num in numbers]
'''
exercise: 2023 J2
'''