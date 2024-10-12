# import turtle
#
# screen = turtle.Screen()
# pen = turtle.Turtle()
#
# shape = screen.textinput('Choose shape',  'Enter a shape (circle, square, triangle):').lower()
# color = screen.textinput('Choose shape', 'Enter a color:')
#
# pen.fillcolor(color)
# pen.begin_fill()
# if shape == 'circle':
#     pen.circle(100)
# elif shape == 'square':
#     pen.forward(100)
#     pen.left(90)
#     pen.forward(100)
#     pen.left(90)
#     pen.forward(100)
#     pen.left(90)
#     pen.forward(100)
#     pen.left(90)
# elif shape == 'triangle':
#     pen.forward(100)
#     pen.left(120)
#     pen.forward(100)
#     pen.left(120)
#     pen.forward(100)
#     pen.left(120)
# else:
#     pen.write('Shape not recognized', font=('Arial', 16, 'normal'))
#
# pen.end_fill()
# turtle.done()

# s = 'abc'
# print(type(s))
#
# s = '123'
# print(type(s))
# a = 123
# print(type(a))

# a = 'hello'
# b = 'world'
# c = a + ' ' + b
# print(c)

# print(1 + 1)
# print('1' + '1')
#
# a = 1
# b = 2
#
# c = a
# a = b
# b = c
#
# print(a)
# print(b)

import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

user_input = input('Enter a word:')
# print(type(user_input))
pen.color('red')
pen.pensize(10)
if user_input == 'star':
    for i in range(5):
        pen.right(144)
        pen.forward(100)

    turtle.done()

