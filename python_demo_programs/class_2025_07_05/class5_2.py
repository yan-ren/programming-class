'''
tuple
list
dictionary
set
'''
# s = set()
# s.add(1)
# print(s)
# s.add(2)
# s.add(1)
# print(s)
#
# s.remove(1)
# value = 3
# if value in s:

l = [1, 2, 1, 2, 4, 3]
l_new = []

# for value in l:
#     if value not in l_new:
#         l_new.append(value)

s = set(l)
print(s)
l_new = list(s)
print(l_new)

# write a function which takes two list as input, return True if there is common value
# return False if not

# union: The union of two sets is a set containing all the distinct elements from both sets.
a = {1, 2, 3}
b = {3, 4, 5}

c = a.union(b)
c = a | b
print(c)

# intersection: The intersection of two sets is a set containing only the elements that are common to both sets.
c = a.intersection(b)
c = a & b
print(c)

# difference: The difference between two sets is a set containing elements that are in the first set but not in the second.
c = a.difference(b)
c = a - b
print(c)

# symmetric difference: The symmetric difference between two sets is a set containing elements
# that are in either of the sets but not in their intersection.
c = a.symmetric_difference(b)
c = a ^ b
print(c)

# def find_common(list1, list2):
#     s1 = set(list1)
#     s2 = set(list2)
#
#     common = s1 & s2
#     if len(common) == 0:
#         return False
#     return True

# Check If All List Elements Are Unique

# l = [1, 3, 2]
# # l.sort()
# l_new = sorted(l, reverse=True)

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# squares = []
# for x in range(10):
#     squares.append(x ** 2)

# squares = [x**2 for x in range(10)]

# sentence = ['and', 'Here', 'HELLO']
# new_sentence = ['and', 'here', 'hello']

# numbers = [1, 2, -1, 3, -4]
# new_numbers = []
#
# for value in numbers:
#     if value > 0:
#         new_numbers.append(value)
#
# new_numbers = [value for value in numbers if value > 0]

# l = []
# for x in range(10):
#     if x % 2 == 0:
#         l.append(x**2)
#     else:
#         l.append(-x)
#
# l = [x**2 if x % 2 == 0 else -x for x in range(10)]

'''
comprehension exercise:
['apple', 'orange', 'pear'] -> ['A', 'O', 'P']
['apple', 'orange', 'pear'] -> [('apple', 5), ('orange', 6), ('pear', 4)]
[1, 2, 3, 4] -> [‘odd’, ‘even’, ‘odd’, ‘even’]
[1, -2, -3, 4] -> [‘positive’, ‘negative’, ‘negative’, ‘positive’]

'''

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

result = [(letter, number) for letter in letters for number in numbers]
