import turtle


game_window = turtle.Screen()
game_window.setup(800, 600)
game_window.bgcolor('chartreuse')

ball = turtle.Turtle()
ball.shape('turtle')
ball.color('red')

# while True:
#     ball.forward(100)
#     ball.left(90)

ball.circle(40)

# ball.penup()

# ball.dy = 0
# ball.dx = 2
#
# while True:
#     ball.dy -= 0.1
#     ball.sety(ball.ycor() + ball.dy)
#
#     if ball.ycor() < -300:
#         ball.dy *= -1
#
#     # bounce on right
#     if ball.xcor() > 400:
#         ball.dx = ball.dx * -1
#     # bounce on left
#     if ball.xcor() < -400:
#         ball.dx = ball.dx * -1
#     ball.setx(ball.xcor() + ball.dx)

turtle.done()
