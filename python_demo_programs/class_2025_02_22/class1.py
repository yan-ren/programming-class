# a = 1 #
# b = 2 #
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b) # float division
# print(a // b) # integer division
# print(a % b)
# print(type(a))
# print(type(b))
# print(a + b)
#
# print((1 + 2) * 3)
# minutes = 42
# seconds = 42
# total_time = minutes * 60 + seconds
# print(total_time)

import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('orange')

pen = turtle.Turtle()

pen.fillcolor('red')
pen.begin_fill()
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.end_fill()

pen.penup()
pen.goto(100, 100)
pen.pendown()
pen.circle(10)
turtle.done()