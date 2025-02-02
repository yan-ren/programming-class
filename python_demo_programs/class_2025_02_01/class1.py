import turtle
# module

wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor('yellow')

ball = turtle.Turtle()
ball.shape('circle')
ball.penup()

ball.dy = 0
ball.dx = 2
count = 0
while True:
    ball.dy = ball.dy - 0.1
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() < -300:
        ball.dy = ball.dy * -1
        count = count + 1
        if count == 2:
            ball.color('red')
    if ball.xcor() > 400:
        ball.dx = ball.dx * -1

turtle.done()