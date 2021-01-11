# practice
# give a list of characters, write a function to remove all duplicate characters from the list
# ["a", "c", "a", "b"] -> ["a", "c", "b"]

# question1: create a list with square of the number from 0 to 10
# [0, 1, 4, 9, .. 100]
# 1. create a list
# 2. loop
# 3. put values into the list base on some conditions
# list = []
# for i in range(11):
#     list.append(i*i)
#
# # question2: give a list of numbers, create a list with only even numbers
# # [1, 2, 3, 4, 5] -> [2, 4]
# '''
# 1. create new list
# 2. loop through the old list
# 3. put the value into new list basing on conditions
# '''
# list = []
# for i in [1, 2, 3, 4, 5]:
#     if i % 2 == 0:
#         list.append(i)
#
# # question3: give a list of numbers, create a list with only positive numbers
# # [1, -2, 3, 4] -> [1, 3, 4]
# '''
# 1. create a new list
# 2. loop through the old list
# 3. put the value into new list basing on conditions
# '''
# list = []
# for i in [1, 2, -1, 3]:
#     if i > 0:
#         list.append(i)

# comprehension
a = [x**2 for x in range(10)]
print(a)

