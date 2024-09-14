import turtle

wn = turtle.Screen()
wn.setup(800, 600)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('green')
ball.penup()
ball.dy = 0
ball.dx = 2

gravity = 0.1

# This is the beginning of the game
# second line
'''
This is a 
multiple
line
comments
'''
while True:
    ball.dy = ball.dy - gravity
    ball.sety(ball.ycor() + ball.dy)

    ball.setx(ball.xcor() + ball.dx)
    if ball.ycor() < -300:
        ball.dy = ball.dy * -1

    if ball.xcor() > 300:
        ball.dx = ball.dx * -1

turtle.done()
