# def greet(name):
#     return 'Hello ' + name
#
# def welcome_user(username):
#     message = greet(username)
#     return message
#
# print(welcome_user('Bob'))

import turtle

wn = turtle.Screen()
wn.setup(800, 800)
wn.bgcolor('yellow')
pen = turtle.Turtle()

# side = 10
# for _ in range(10):
#     for _ in range(4):
#         pen.forward(side)
#         pen.left(90)
#         side += 2
pen.penup()
pen.goto(100, 100)

pen.pendown()
pen.color('red')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
turtle.done()
