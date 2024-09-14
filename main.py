import turtle

wn = turtle.Screen()
wn.setup(800, 600)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('green')
ball.penup()
ball.dy = 0

gravity = 0.1

while True:
    ball.dy = ball.dy - gravity
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -300:
        ball.dy = ball.dy * -1

turtle.done()
