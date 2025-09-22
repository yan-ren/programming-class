# print(1 + 2)

import turtle

wn = turtle.Screen()
wn.setup(600, 800)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()

ball.dy = 0
ball.dx = 2

while True:
    ball.dy -= 0.2
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() < -200:
        ball.dy *= -1

    if ball.xcor() > 200 or ball.xcor() < -200:
        ball.dx = ball.dx * -1