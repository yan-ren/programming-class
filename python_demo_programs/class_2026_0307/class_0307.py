'''
variable
- integer
- float
math
+ - * /
% mod (gives the remainder)
**

- string
- boolean
    - True False
    - and or not

input() - console I/0

if statement

loop statement
- while
- for
'''
# a = 2
# b = 3
# print(a / b)
# print(a // b)
#
# print(a % b)
#
# s = "abcefgh"
# print(len(s))
# print(s[0])
# print(s[4])
# print(s[-1])
# print(s[len(s) - 1])
# print(s[2:5])
# print(s[:5])
# print(s[3:])
# print(s[1:5:2])

'''
write a program asking user for input number, tell them it's positive, negative or zero
and check even or odd
'''
# number = int(input('Enter a number:'))
# if number > 0:
#     print('positive')
# elif number < 0:
#     print('negative')
# else:
#     print('zero')
#
# if number % 2 == 0:
#     print('even')
# else:
#     print('odd')

'''
= vs ==
'''
# a = 1
# b = 3
# c = (a > 2 and a == b)
# print(type(c))
# print(c)
# first = int(input())
# second = int(input())
# third = int(input())
#
# # nested if statement
# if first > second:
#     if first > third:
#         print('first is the largest')
#     else:
#         print('third is the largest')
# else:
#     if second > third:
#         print('second is the largest')
#     else:
#         print('third is the largest')
#
# # if first > second > third:
#
# if first > second and first > third:
#     print('first is the largest')
# elif second > first and second > third:
#     print('second is the largest')
# else:
#     print('third is the largest')

i = 1
while i <= 10:
    print(i)
    i += 1

for i in range(1, 11):
    print(i)


numbers = [1, 2, 4, 2]
for num in numbers:
    print(num)
'''
for 
+ range
+ string
+ list
+ dictionary
'''

s = 'abcd12345'

for ch in s:
    print(ch)

