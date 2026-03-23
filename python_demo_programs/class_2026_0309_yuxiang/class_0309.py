'''
Python
- basic coding (basic logic + native library):
- analysis (panda, numpy, mataplot)
- spark?
'''
'''
basic type:
- int
- float
- string
- boolean

advanced type:
'''
# dynamic typing
# x = 0
# print(type(x))
# y = 0.0
# print(type(y))
#
# x = 2
# y = 3
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y) # float division
# print(x // y) # integer division
#
# print(x % y) # mod [0, y-1]
# print(0.1 + 0.2)
#
# from decimal import Decimal
#
# a = Decimal('0.1')
# b = Decimal('0.2')
# print(a + b)
#
# s = 'abcde123'
# a = '123'
# b = 123
# # print(a + b)
#
# print(len(s))
# s = 'He said: "hello"'
# greeting = 'Hello'
# group = 'World'
#
# print(greeting + ' ' + group)
#
# a = '1'
# b = '1'
# print(a + b)
#
# a = 1
# b = 1
# print(a + b)

# x = True
# y = False
# print(type(x))
# print(type(y))
# print(int(x))
# print(int(y))
#
# z = 12
# z_s = str(z)
# print(type(z_s))

# a = 1
# b = 2
#
# print(a == b)
# print(a != b)
# print(a > b)

# and: one false, overall is false
# a = True
# b = False
# c = a and b

# or: one true, overall is true
# c = a or b
# print(c)

# not
# c = not a
# print(c)
#
# name = input('Enter your name:')
# print('Hello ' + name)

'''
if statement
loop:
- for
- while
'''

# first = int(input('Enter the first number:'))
# second = int(input('Enter the second number:'))
#
# if first > second:
#     print('first number is the largest')
# elif second > first:
#     print('second number is the largest')
# else:
#     print('same')

number = 101

if number > 0:
    print('number is bigger than 0')
elif number > 10:
    print('number is bigger than 10')
elif number > 100:
    print('number is bigger than 100')

# correct
if number > 100:
    print('number is bigger than 100')
elif number > 10:
    print('number is bigger than 10')
elif number > 0:
    print('number is bigger than 0')