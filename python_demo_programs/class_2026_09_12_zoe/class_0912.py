import turtle


wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.bgcolor('skyblue')

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()

ball.goto(0,100)

ball.dy = 0 # delta, how much we want to change the y value
gravity = 0.2

ball.dx = 2

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    # ycor() -> get the y coordinate
    if ball.ycor() < -200:
        ball.dy *= -1

    ball.setx(ball.xcor() + ball.dx)
    if ball.xcor() > 200:
        ball.dx = ball.dx * -1

turtle.done()