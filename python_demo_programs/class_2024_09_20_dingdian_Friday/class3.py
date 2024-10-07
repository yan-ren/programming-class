# conditional
# first = int(input('Enter the first number:'))
# second = int(input('Enter the second number:'))
# if first > second:
#     print('First number is bigger')
# elif second > first:
#     print('Second number is bigger')
# else:
#     print('Two numbers are the same')

# ask user a number, tell people the number is positive or negative or zero
# number = int(input('enter a number'))
# if number > 0:
#     print('positive')
# elif number < 0:
#     print('negative')
# else:
#     print('zero')

# print('You enter a dark room with two doors. Do you go through door #1 or door #2?')
#
# door = input('>')
# if door == '1':
#     print('There is a giant bear here eating a cheese cake')
#     print('What do you do?')
#     print('1. Take the cake')
#     print('2. Scream at the bear')
#
#     bear = input('>')
#
#     if bear == '1':
#         print('The bear eats your face off')
#     elif bear == '2':
#         print('The bear eats your legs off')
#     else:
#         print('Bear runs away')
# elif door == '2':

import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

shape = screen.textinput('Choose shape',  'Enter a shape (circle, square, triangle):').lower()

if shape == 'circle':
    pen.circle(100)
elif shape == 'square':
    pass
elif shape == 'triangle':
    pass
else:
    pen.write('Shape not recognized', font=('Arial', 16, 'normal'))

turtle.done()
