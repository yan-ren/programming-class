d1 = {"A": 1, "B": 2}
d2 = {"C": 3}

# {"A": 1, "B": 2, "C": 3}
d3 = {}
# for key, value in d1.items():
#     d3[key] = value
#
# for key, value in d2.items():
#     d3[key] = value

# unpack
# test = (1, 2, 3)
# a, b, c = test
#
# d3 = {**d1, **d2}
#
# number = 100_000_000
# print(number + 1)

# lst = ["Nepal", "Bhutan", "Korea", "Vietnam"]
# str = ','.join(lst)
# print(str)
#
# str1 = "hello"
# str2 = str1 * 5
#
# str = "hello world"
# l = str.split(" ")
# print(l)
#
# list = [1, 2, 3, 4]
# list.reverse()

# a = 1
# b = 2
# # print(a, b, sep="", end='')
#
# print('one', end='')

# list comprehension
# shortcut to create a list
# list = [1, 2, 3, 4]
# list2 = []
# for i in list:
#     list2.append(i**2)
#
# list2 = [i**2 for i in list]
#
# list = [1, -2, 1, -3]
#
# [-i if i < 0 else i for i in list]
# # [1, 2, 1, 3]

'''
today:

review

python turtle
- graph, pattern
'''

# variable
# string, integer, float, boolean

# integer/float -> number -> math
# boolean -> if/while -> conditional
# a = 10
# if a > 0:
#     print()
#
# # string -> quote ->
# s = "abcabcdeabcabcdedeabcabcdedede"
#
# a = 100
# if a > 10:
#     print('a is bigger than 10')
# elif a < 10:
#     print('a is smaller than 10')
# else:
#     print('a is equal to 10')
#
# while a > 10:
#     print(a)
#     a += 1

# list
numbers = []
print(numbers)
numbers.append(1)
numbers.append(2)
print(numbers)

# remove in list by value
numbers.remove(1)

# remove by index
del numbers[0] # delete the value at index 0

len(numbers)

# given a list, check if there is duplicated value in the list
'''
list = [1, 2, 3, 1]
print True

list = [1, 2, 3]
print False
'''
# list = [1, 2, 3, 1]
# i = 0
# while i < len(list):
#     j = i + 1
#     while j < len(list):
#         if list[i] == list[j]:
#             print(True)
#         j += 1
#     i += 1



