# print(1 + 2)

import turtle

wn = turtle.Screen()
wn.setup(600, 800)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()

ball.dy = 0

while True:
    ball.dy -= 0.1
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -200:
        ball.dy *= -1