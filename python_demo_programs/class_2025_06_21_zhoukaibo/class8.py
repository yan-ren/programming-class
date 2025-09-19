'''
data structure: list
'''
# grades = [90, 91, 20, 89]
# grades.append(99)
# print(grades)

# s = 'abcdef'
# print(s[0])

# print(grades[0])
# print(grades[2])
# print(grades[len(grades) - 1])
#
# grades.remove(91)
# del grades[0]

# if 91 in grades:
#     grades.remove(91)

# numbers = [1, 2, 10, 4, 2, 5]
# s = 0
# for num in numbers:
#     s += num
#
# print(s)

# find the largest value from the list

'''
Given a list of value, numbers = [4, 2, 3, 6]
generate a reversed list, [6, 3, 2, 4]
'''
numbers = [4, 2, 3, 6]
new_numbers = []
index = len(numbers) - 1
while index >= 0:
    new_numbers.append(numbers[index])
    index -= 1

'''
Given a list of numbers = [1, 20, -3, 2]
create a new list with only positive values [1, 20, 2]

Given a list of numbers = [1, 2, 1, 3, 2, 2, 2]
create new list without duplicates [1, 2, 3]
'''
numbers = [1, 20, -3, 2]