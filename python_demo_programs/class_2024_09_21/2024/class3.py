'''
s = 'abcd'
'''
# s = '123'
# print(type(s))
#
# n = 123
# print(type(n))

# conditional - continue
# a = int(input('Enter the first value:'))
# b = int(input('Enter the second value:'))
# if a > b:
#     print('The first value is bigger') # indentation
# elif b > a:
#     print('The second value is bigger')
# else:
#     print('They are the same')

# ask user a number, check if positive, negative or zero
# number = int(input('Enter a number:'))
#
# if number > 0:
#     print('positive')
# elif number < 0:
#     print('negative')
# else:
#     print('zero')

# first = int(input('Enter the first value:')) #4
# second = int(input('Enter the second value:')) #2
# third = int(input('Enter the third value:')) #3

# not working
# if first > second > third:
#     print('first value is the largest')
# elif second > first > third:
#     print('second value is the largest')
# else:
#     print('third value is the largest')

# if first > second:
#     if first > third:
#         print('first is the biggest')
#     else:
#         print('third is the biggest')
# else:
#     if second > third:
#         print('second is the biggest')
#     else:
#         print('third is the biggest')

# if first > second and first > third:
#     print('first is the biggest')
# elif second > first and second > third:
#     print('second is the biggest')
# else:
#     print('third is the biggest')

# decision game
# print('You enter a dark room with two doors. Do you go through door 1 or door 2')
#
# door = input('>')
#
# if door == '1':
#     print('There is a giant bear here eating a cheese cake.')
#     print('what do you do?')
#     print('1. Take the cake')
#     print('2. Scream at the bear')
#
#     bear = input('>')
#     if bear == '1':
#         print('The bear eats your face off')
#     elif bear == '2':
#         print('The bear eats your legs off')
#     else:
#         print('Bear runs away')
# elif door == '2':
    # continue

import turtle


screen = turtle.Screen()
pen = turtle.Turtle()

shape = screen.textinput('Select shape', 'Choose from circle and triangle')
color = 'red'

pen.fillcolor(color)
pen.begin_fill()
if shape == 'circle':
    pen.circle(100)
elif shape == 'triangle':
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.left(120)

pen.end_fill()
turtle.done()
# 1. add another textinput asking for color
# 2. add more shape options