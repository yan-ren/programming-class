'''
data structure
- list
- dictionary
- set
- tuple
'''

# list -> Array List, linked list
# mutable

# tuple -> array
# immutable

# numbers = [2, 1, 3, 4]
# numbers[3] = 5

# numbers = (2, 1, 3, 4)
# print(type(numbers))
#
# for num in numbers:
#     print(num)
#
# print(numbers[0])
# numbers[0] = 20

# numbers = 2, 1, 3, 4

# def calculation(a, b):
#     return a + b, a - b
#
# result = calculation(1, 2)
# print(type(result))
# print(result)

# set: math concept, a group of unique value
# s = {1, 2, 3, 1}
# print(s)

# a = [1, 2, 2, 3, 4]
# task: create a list without duplicates
# a_new = []
#
# for num in a:
#     if num not in a_new:
#         a_new.append(num)
# print(a_new)

# s = set(a)
# a_new = list(s)
# print(a_new)

# s = {'one': 1}
# s = {1, 2, 3}
# s.add(4)
# s.remove(2)
#
# if 3 in s:
#     print('exist')

a = {1, 2, 3}
b = {3, 4, 5}
c = a | b # union
print(c)

c = a & b # intersection
print(c)

c = a - b # difference
print(c)

# Check if Two Lists Have Any Common Elements
a = [1, 2, 3]
b = [4, 5, 3]
# write a function takes two lists as input, return true if they have common value, or false if not
def has_common(a, b):
    a = set(a)
    b = set(b)
    c = a & b
    if len(c) > 0:
        return True
    return False
