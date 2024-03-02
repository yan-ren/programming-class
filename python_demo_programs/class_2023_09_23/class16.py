# table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for row in table:
#     for value in row:
#         print(value)
#
import time
# for row in range(1, 11):
#     for value in range(1, row+1):
#         print(row * value, end = " ")
#     print()

import turtle

wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor('black')
wn.tracer(0)

# left paddle
left_paddle = turtle.Turtle()
left_paddle.shape('square')
left_paddle.shapesize(5, 1)
left_paddle.penup()
left_paddle.color('white')
left_paddle.goto(-350, 0)
left_paddle.speed(0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.shape('square')
right_paddle.shapesize(5, 1)
right_paddle.penup()
right_paddle.color('white')
right_paddle.goto(350, 0)
right_paddle.speed(0)

# ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.speed(0)
ball.dx = 0.01
ball.dy = 0.01

left_paddle_score = 0
right_paddle_score = 0

# pen
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('white')
pen.speed(0)
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(left_paddle_score, right_paddle_score), align="center", font=('Courier', 24, 'bold'))

def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)


def right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 20)


def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 20)


wn.onkeypress(left_paddle_up, 'w')
wn.onkeypress(left_paddle_down, 's')
wn.onkeypress(right_paddle_up, "Up")
wn.onkeypress(right_paddle_down, "Down")
wn.listen()

# main game loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy = -ball.dy

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx = -ball.dx

    if ball.xcor() < left_paddle.xcor() + 5 and left_paddle.ycor() - 60 < ball.ycor() < left_paddle.ycor() + 60:
        ball.dx = -ball.dx
    if ball.xcor() > right_paddle.xcor() - 5 and right_paddle.ycor() - 60 < ball.ycor() < right_paddle.ycor() + 60:
        ball.dx = -ball.dx

    # left paddle score
    if ball.xcor() > 390:
        left_paddle_score += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(left_paddle_score, right_paddle_score), align="center",
                  font=('Courier', 24, 'bold'))

    # right paddle score
    if ball.xcor() < -390:
        right_paddle_score += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(left_paddle_score, right_paddle_score), align="center",
                  font=('Courier', 24, 'bold'))
