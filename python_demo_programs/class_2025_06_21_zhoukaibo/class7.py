'''
Last time: Python String
'''
from python_demo_programs.class_2023_09_23.class13 import is_prime

s = 'abcd'
# s[0] = 'c' # immutable
# print(s)

# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1

# for c in s:
#     print(c)

# for i in range(10):
#     print(i)
#
# for i in range(1, 10):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)

# 1 + 2 + ... + 100 using for loop
# s = 0
# for i in range(1, 101):
#     s += i
#
# print(s)

# prime number checking
# number = int(input('Enter a number for prime checking:'))
#
# is_prime = True
#
# for i in range(2, number):
#     if number % i == 0:
#         is_prime = False
#
# print(is_prime)

# factorial 5! = 5 * 4 * 3 * 2 * 1

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i, '*', j, '=', i * j)

# break/continue
# i = 0
# while i < 10:
#     print(i)
#     if i == 3:
#         i += 1
#         continue
#     i += 1

'''
1
2
4
5
'''
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1