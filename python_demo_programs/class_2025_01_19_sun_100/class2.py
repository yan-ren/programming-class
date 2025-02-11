# # import turtle
#
# wn = turtle.Screen()
# wn.setup(800, 600)
#
# # exercise: draw a triangle
# pen = turtle.Turtle()
# pen.color('red')
#
# pen.begin_fill()
# pen.forward(100)
# pen.left(120)
# pen.forward(100)
# pen.left(120)
# pen.forward(100)
# pen.left(120)
# pen.end_fill()
#
# # pen.setheading(90)
#
# # pen.color()
#
# turtle.done()

# a = 1
# b = 2
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(type(1))
# print(type(1.0))
# print(2 ** 3)

# special
# print(a // b)
# print(7 % 3)

# print(1)
# name = input('Enter your name:')
# print('Welcome', name)
#
# age = int(input('Enter your age:'))
# print('Next year, you are', age + 1)
# if age < 18:
#     print('')
#
# food = input('What do you like to eat:')
# if food == 'hamburger':
#     print('not healthy')
# elif food == 'banana':
#     print('good for monkey')
# else:
#     print()

import turtle

wn = turtle.Screen()
wn.setup(800, 600)

pen = turtle.Turtle()
pen.color('yellow')

pen.penup()
pen.goto(-200, 200)

pen.begin_fill()
pen.circle(20)
pen.end_fill()

turtle.done()