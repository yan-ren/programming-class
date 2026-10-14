import turtle

# bouncing ball programming
window = turtle.Screen()
window.bgcolor("black")
window.setup(800, 600)

ball = turtle.Turtle()
ball.shape('circle')
ball.color("white")
ball.penup()

ball.dy = 0
gravity = 0.1

while True:
    ball.dy -= gravity

    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -300:
        ball.dy *= -1

turtle.done()