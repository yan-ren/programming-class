'''
dictionary
pair: key - value
always work with value through key
key cannot be duplicated
'''
import sys


# d = {'Alice': 90}
# d['Bob'] = 70
#
# print(d['Bob'])
#
# # d = {1: 'a', 2: 'b', 'c': 3}
#
# del d['Bob']
#
# for k in d:
#     print(k)
#
# for v in d.values():
#     print(v)
#
# for k, v in d.items():
#     print(k, v)


# def statistic(marks):
#     min = sys.maxsize
#     max = -sys.maxsize - 1
#     for k, v in marks.items():
#         if v > max:
#             max = v
#         if v < min:
#             min = v
#
#     return max, min
#
# marks = {'Alice': 90, 'Bob': 65, 'Tom': 70}

# find the most frequent letter from the string
s = 'abbbcabd'
# 1. how to count each character
# d = {}
# for ch in s:
#     if ch in d:
#         d[ch] += 1
#     else:
#         d[ch] = 1
# print(d)
# 2. how to find which character is most frequent

d1 = {'a': 1, 'b': 3, 'c': 12}
d2 = {'b': 2, 'e': 4}

'''
d = {'a': 1, 'b': [3, 2], 'c': 12, 'e': 4}
'''
# d = {}
# for k, v in d1:
#     if k in d:
#         d[k].append(v)
#     else:
#         d[k] = [v]

roster = {
    'Alice': {'Math': 'A', 'English': 'B'},
    'Bob': {'Math': 'C', 'History': 'A', 'Science': 'B'},
    'Charlie': {}
}

print(roster['Bob']['Math'])

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)

words = ['eat', 'tea', 'ate']

'''
Given a dictionary where values may be duplicated, 
create a new dictionary that maps each value to a list of keys that had that value.

input_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2
}

output_dict = {
    1: ['a', 'c'],
    2: ['b', 'e'],
    3: ['d']
}
'''