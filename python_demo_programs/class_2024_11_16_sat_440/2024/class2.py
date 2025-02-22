'''
Variable:

name = value

basic value:
-   integer: number without decimal point
-   float: number with decimal point
-   boolean: True/False
-   string
'''

# age = 12
# print(age)
# print(type(age))

# a = 1
# b = 1.0
#
# print(type(a))
# print(type(b))
#
# print(7 / 2)
# print(7 // 2)
#
# print(2 ** 3)
# print(7 % 3)
# print(3 % 2)
# print(2 % 3)
# print(4 % 2)

# name = input('Please enter your name: ')
# print('Hello', name)
# print(type(name))

# ask user for three number, print the largest number
# first = int(input('Enter first number: '))
# second = int(input('Enter second number: '))
# third = int(input('Enter third number: '))

# if first > second and first > third:
#     print(first)
# elif second > first and second > third:
#     print(second)
# else:
#     print(third)

'''
nested if statement
'''
# if first > second:
#     if first > third:
#         print(first)
#     else:
#         print(third)
# else:
#     if second > third:
#         print(second)
#     else:
#         print(third)

'''
ask user for a number, print it's even or odd
'''

# a = True
# a = 1
# b = 1
# print(a == b)
# print(a != b) # not equal
#
# # not and or
# a = False
# b = True
# c = a or b

'''
character: letter, number, special character
'''
# s = '' # empty string
# print(s)
#
# s = 'hello'
# t = 'world'
# n = 1
#
# new = s + ' ' + t + str(n)
# print(new)

'''
Ask user for a string that represents as a password
check if password is within 8-10 characters long
if too short, print too short
if too long, print too long
if within 8-10 characters, print valid
'''

s = 'Arthur'
print(s[3])
print(s[5])
# print(s[6])
print(s[0:2])
print(s)

'''
Exercise: Palindrome Check
Write a program that:

Takes a string input from the user.
Checks if the string is a palindrome (reads the same backward as forward).
Example of a palindrome: "radar", "level".
'''

# text = input('Enter a string for palindrome checking:')
# text_rev = text[::-1]
#
# if text == text_rev:
#     print('Palindrome')
# else:
#     print('Not palindrome')
