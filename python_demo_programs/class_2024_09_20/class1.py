# x = 1
# y = 2
#
# print(x + y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x - y)
#
# name = input('what is your name:')
# print('your name is', name)
#
# if name == 'Tom':
#     print('hello Tom')
# elif name == 'Jerry':
#     print('hello Jerry')
# else:
#     print('who are you?')

import turtle

window = turtle.Screen()
window.setup(800, 800)

t = turtle.Turtle()

t.fillcolor('red')

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

turtle.done()