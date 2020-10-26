# # write a python function that takes a list and a int, check if list contains any two values that diff of the two values
# # is the input int
# # [1, 2, 3] 1 -> true
# # [1, 2, 3] 4 -> false
#
# def find_diff(list, target):
#     for i in list:
#         for j in list:
#             if j - i == target:
#                 return True
#
#     return False
#
#
# l = ["1", "2", "3"]
# print(l)
# l[0] = 100
# print(l)
#
# s = 'abc'
# # question: what's the similar part between list and string
# # 1. contains multiple items
# # [1, 2, 3] '123'
# # 2. index
# # 3. loop
# # 4. len()
# # different: list -> mutable(changeable), string -> immutable(unchangeable)
#
# list = [1, 2, 3]
#
# string = 'abc'
# # string[0] = 'w'
#
# string_new = string + 'w' # this does not change the string, it creates a new string
# print(string)
# print(string_new)
#
# print(list.count(3))

# a = [1, 2, 3]
b = 1, 2, 3
# print(type(a))
print(type(b))
x, y = b
# unpack
print(x)
print(y)
# print(z)

# # write a function takes a list and tuple, check if all values in tuple also in the list
# def contains(l, t):
#     for i in t:
#         if i not in l:
#             return False
#     return True
#
# # write a function that takes a tuple as input, return a list contains the same value as tuple
# def tuple_to_list(tuple):
#     list = []
#     for i in tuple:
#         list.append(i)
#     return list

# write a function that takes a list and a value, delete all the values from list which is equal to the given value
# [1, 2, 2, 3] 2 -> [1, 3]