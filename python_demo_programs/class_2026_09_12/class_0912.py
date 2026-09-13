import turtle


wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.bgcolor('skyblue')

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()

ball.goto(0,100)

ball.dy = 0
gravity = 0.1

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() < -200:
        ball.dy *= -1

turtle.done()