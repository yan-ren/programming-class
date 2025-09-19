'''
*
**
***
****

Write a loop that calculates the total of the following series of numbers:
(1 / 50) + (2 / 49) + (3 / 48) + (4 / 47) + ...+ (48 / 3) + (49 / 2) + (50 / 1)
'''

# row = 1
# while row <= 4:
#     col = 0
#     while col < row:
#         print('*', end='')
#         col += 1
#     row += 1
#     print()
#
# num = 1
# sum = 0
# while num <= 50:
#     sum = sum + (num / (51 - num))
#     num += 1
#
# print(sum)

# range(10) -> 0, 1, 2, ..., 9
# for i in range(10):
#     print(i)
#
# for i in range(1, 10):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)for i in range(10):
#     print(i)
#
# for i in range(1, 10):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)

# for i in range(10, 1, -1):
#     print(i)

# s = 'abc123'
# for letter in s:
#     print(s)

# exercise: print all number under 100 that can be divided by 5, using for loop
# for num in range(101):
#     if num % 5 == 0:
#         print(num)

# exercise: given a string, create a new reversed string
# 'abc' -> 'cba'
# word = 'abc'
# new_word = ''
#
# for letter in word:
#     new_word = letter + new_word
#
# print(new_word)

# exercise: given a string, count how many vowels inside, using for loop
# e.g. 'hello' -> 2