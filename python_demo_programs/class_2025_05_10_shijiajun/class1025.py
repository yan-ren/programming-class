'''
data type:
- int
- float
- boolean
    - if elif else
- string
'''
# a = 3
# b = 2
#
# print(a / b)
# print(a // b)
#
# print(a % b)
#
# s = 'acd1233!@#'
#
# # if statement
# if a > 100:
#     print('a is bigger than 100')
# elif a > 10:
#     print('a is bigger than 10')
#
# # loop
# # for
# for i in range(1, 11):
#     print(i)
#
# # while
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# l = [1, 2, 1, 4]

N = int(input())
C = int(input())
P = int(input())

if N > C * P:
    print('no')
else:
    print('yes')