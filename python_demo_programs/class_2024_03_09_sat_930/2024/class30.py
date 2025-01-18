'''
Python basic data structure

list
tuple
dictionary
set

set: unique elements
'''

numbers = {1, 2, 3, 5}
# numbers = set() # create an empty set
numbers.add(1)
numbers.remove(5)

print(numbers)

numbers = list(numbers)
print(numbers)

'''
Given a list of numbers, e.g. [1, 2, 1, 1, 4, 2]
remove the duplicate value from the list
'''
numbers = [1, 2, 1, 1, 4, 2]

# numbers = list(set(numbers))
#
# print(numbers)

# new_numbers = []
#
# for num in numbers:
#     if num not in new_numbers:
#         new_numbers.append(num)
#
# print(new_numbers)

# seen = set()
#
# print([num for num in numbers if num not in seen and not seen.add(num)])


# d = {'one': 1, 'two': 2}
# d = {} # create an empty dictionary

s = 'hello welcome hellohello hi'
print(s.count('hello'))
print(s.index('hello'))

# 'welcome' in s # boolean, true or false
