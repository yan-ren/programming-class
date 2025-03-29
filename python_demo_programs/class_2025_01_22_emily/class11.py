'''
4 basic data structure in python
- list
- dictionary
- tuple
- set

real life
word - sentence

coding
key - value
'''

ages = {}
ages['Tom'] = 16
ages['Jerry'] = 15
print(ages)
print(ages['Tom'])
ages['Tom'] = 19
print(ages)

# del ages['Tom']
ages.pop('Tom')
print(ages)

# check if a key exists in dictionary
# if 'Jerry' in ages:

# loop through a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
# loop by key
for k in d:
    print(k, d[k])

# loop by value:
for v in d.values():
    print(v)

# most common way loop by pair
for k, v in d.items():
    print(k, v)

# s = 'aabbcabccb'
# # d = {'a': 3, 'b': 4, 'c': 3}
# d = {}
#
# for c in s:
#     if c in d:
#         d[c] += 1
#     else:
#         d[c] = 1
#
# print(d)
#
# max_v = 0
# max_k = ''
# for k, v in d.items():
#     if v > max_v:
#         max_v = v
#         max_k = k
#
# print(max_k)

# how to determine if a list contains the duplicated value
numbers = [1, 2, 3, 4, 5, 5]

# def is_duplicate(numbers):
#     for i in range(len(numbers)):
#         for j in range(i, len(numbers)):
#             if numbers[i] == numbers[j]:
#                 return True
#
#     return False

def is_duplicate(numbers):
    seen = {}

    for num in numbers:
        if num in seen:
            return True
        seen[num] = 1

    return False

import numpy as np

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)

# array: equivalent as list but used in numpy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b) # linear algebra: vector addition

