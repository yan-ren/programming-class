# fruits = {'apple', 'banana', 'cherry'}
# fruits.add('apple')
#
# print(fruits)
from os.path import commonpath

from class_2024_04_27.class3 import score_1

# numbers = [1, 2, 2, 3, 4, 4, 5]
# s = set()
#
# for num in numbers:
#     s.add(num)
#
# new_numbers = []
#
# for num in s:
#     new_numbers.append(num)
#
# numbers.remove(4)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)        # or a.union(b)
print("Intersection:", a & b) # or a.intersection(b)
print("Difference:", a - b)   # or a.difference(b)
print("Symmetric Diff:", a ^ b) # or a.symmetric_difference(b)


# find how many unique character in string
s = 'hello'

# Check for common elements, given two lists, check if they have any elements in common
list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 8]
# Expected Output: True (because of 3)

s1 = set(list1)
s2 = set(list2)

common = s1 & s2

if len(common) > 0:
    print(True)
else:
    print(False)


'''
Problem: Write a function that checks if two strings share at least one common character.

str1 = "hello"
str2 = "world"

Expected Output: True (common letter: "l" or "o")
'''

str1 = "hello"
str2 = "world"

s1 = set()
s2 = set()

for letter in str1:
    s1.add(letter)

for letter in str2:
    s2.add(letter)

common = s1 & s2

if len(common) > 0:
    print(True)
else:
    print(False)