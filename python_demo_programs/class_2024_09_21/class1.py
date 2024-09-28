# print('hello')

# x = 1
# y = 1.0
#
# print(type(x))
# print(type(y))

# integer is the number without the decimal point
# float is the number with the decimal point

# x = 1
# y = 2
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y) # float division gives result in float
# print(x // y)
#
# print(2 ** 4)
# print(5 % 2)

import turtle

window = turtle.Screen()
window.setup(800, 800)

t = turtle.Turtle()

t.fillcolor('red')

t.begin_fill()
# t.left(90)
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