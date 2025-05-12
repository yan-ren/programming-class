# from matplotlib import pyplot
# from matplotlib.pyplot import *

# numpy is a python library better for solving math problem, it enhances basic python feature for math usage
# numbers = np.array([1, 2, 3, 4, 5]) # np.array is basic numpy component, similiar as python list but has more feature
# print(numbers)
# A = np.array([[1, 2], [2, 3]])
# B = np.array([[4, 5], [6, 7]]) # matrix - math
#
# print(A + B)
#
# A = [[1, 2], [2, 3]]
# B = [[4, 5], [6, 7]]
# print(A + B)

# numbers = []
# for i in range(10):
#     numbers.append(0)
#
# print(numbers)

# list comprehension - shortcut
# numbers = [0 for i in range(10)]
# print(numbers)

# def transpose(matrix):
#     n_lines = len(matrix)
#     n_columns = len(matrix[0])
#
#     transpose = []
#     for i in range(n_columns):
#         line = []
#         for j in range(n_lines):
#             line.append(0)
#         transpose.append(line)
#
#     for i in range(n_lines):
#         for j in range(n_columns):
#             transpose[j][i] = matrix[i][j]
#
#     return transpose
#
# matrix = [[1, 2],
#           [3, 4],
#           [5, 6]]
#
# print(transpose(matrix))

'''
f(x) = 2xsin(4x) + cos (2x) 
g(x) = 4*6x^2 + ln (x)
'''
# import numpy as np
#
# x = np.linspace(1, 100, 400)
# y_f = 2 * np.sin(4*x) + np.cos(2*x)
# y_g = 6*x*x + np.log(x)
#
# plt.figure(figsize=(12, 8))
# plt.plot(x, y_f, 'r', label="f(x)")
# plt.plot(x, y_g, 'g', label="g(x)")
# plt.xlabel("x")
# plt.ylabel("f(x)/g(x)")
# plt.legend()
# plt.show()

# s = 'abcdeaabcde'
# d = {}
#
# for ch in s:
#     if ch in d:
#         d[ch] += 1
#     else:
#         d[ch] = 1
#
# print(d)
#
# max_value = -1
# max_ch = None
#
# for key, value in d.items():
#     if value > max_value:
#         max_value = value
#         max_ch = key
#
# print(max_ch)

# kayak
# when i = 0 - 4
# when i = 1 - 3
# def palindrome(s):
#     for i in range(len(s) // 2):
#         if s[i] != s[len(s) - 1 - i]:
#             return False
#
#     return True

# with open('data.txt', 'r') as file:
#     # context = file.read()
#     line_number = 0
#     for line in file:
#         print(line_number, line)
#         line_number += 1
# # print(context)

# s = '\n\nhello\n\n'
# print(s)
# print(s.strip())

s = 'abc'
print(s.split()) # separate by whitespace
print(list(s))

s = 'a,b,c'
print(s.split(','))