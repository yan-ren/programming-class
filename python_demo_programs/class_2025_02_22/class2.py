# name = input('Enter your name:')
# print(type(name)) # '123' 123
# print('You enter', name)

# number = int(input('Enter a number:'))
#
# if number > 0:
#     print('positive')
# elif number < 0:
#     print('negative')
# else:
#     print('zero')

first = int(input('Enter the first number:'))
second = int(input('Enter the second number:'))
third = int(input('Enter the third number:'))

# nested if statement
if first > second:
    if first > third:
        print('first is largest')
    else:
        print('third is largest')
else:
    if second > third:
        print('second is largest')
    else:
        print('third is largest')

#
# if first > second and first > third:
#     print('first is largest')
# elif second > first and second > third:
#     print('second is largest')
# else:
#     print('third is largest')

# exercise: ask user for a number, and determine it's even or odd
# exercise: turtle+input+if: ask user for a shape, turtle draws the shape according

import turtle

screen = turtle.Screen()

shape = screen.textinput('Enter the shape:', 'Enter the shape:')
# if shape == 'circle':