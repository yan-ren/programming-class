import turtle

screen = turtle.Screen()
screen.setup(800, 600)

ball = turtle.Turtle()
ball.shape('circle')
ball.penup()
ball.goto(0, 100)
ball.dy = 0
gravity = 0.1
ball.dx = 2

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -300:
        ball.dy = ball.dy * -1

    ball.setx(ball.xcor() + ball.dx)
    if ball.xcor() > 300:
        ball.dx = ball.dx * -1
    if ball.xcor() < -300:
        ball.dx = ball.dx * -1

turtle.done()