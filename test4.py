'''
bouncing ball
'''
import time
import turtle


wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor('cyan')

ball = turtle.Turtle()
ball.shape('circle')
ball.penup()

ball.speed(0)
ball.goto()

ball.dy = 0
ball.dx = 2
wn.tracer(0)

while True:
    wn.update()
    time.sleep(0.01)

    ball.dy -= 0.1
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -300:
        ball.dy = ball.dy * -1

turtle.done()
