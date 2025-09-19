'''
basic types

int
float
string
boolean

list
dictionary
set
...

'''
# a = 1
# print(type(a))
#
# b = 1.2
# print(type(b))

# print(1 + 1)
# print(5 / 2)  # float division
# print(5 // 2) # integer division
# print(7 % 2)
# print(5 % 3)

# print(4 % 2) # even number
# print(5 % 2) # odd number
# print(2 ** 4)
#
# print(1.0 + 1)

# minutes = 42
# seconds = 42
# print(seconds + minutes * 60)

import turtle # module


window = turtle.Screen()
window.setup(800, 800)
# window.bgcolor('black')

ball = turtle.Turtle()
ball.shape('circle')
ball.color('green yellow')
ball.penup()

ball.dy = 0
gravity = 0.05

ball.dx = 2

while True:
    ball.dy = ball.dy - gravity
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() < -400:
        ball.dy = ball.dy * -1

    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.dx = ball.dx * -1

turtle.done()