import turtle

game_window = turtle.Screen()
game_window.setup(800, 600)
game_window.bgcolor('black')

ball = turtle.Turtle()
ball.shape('turtle')
ball.color('red')

# ball.forward(100)
# ball.left(90)
# ball.forward(100)
# ball.left(90)
# ball.forward(100)
# ball.left(90)
# ball.forward(100)
# ball.left(90)

ball.penup()

ball.dy = 0
gravity = 0.1

ball.dx = 2

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -200:
        ball.dy = ball.dy * -1

    ball.setx(ball.xcor() + ball.dx)
    if ball.xcor() > 200:
        ball.dx = ball.dx * -1
    if ball.xcor() < -200:
        ball.dx = ball.dx * -1


turtle.done()
