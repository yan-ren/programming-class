import turtle

window = turtle.Screen()
window.bgcolor('black')
window.setup(800, 600)
window.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(5, 1)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(5, 1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(6)
ball.shape('square')
ball.color('white')
ball.penup()
ball_x_change = 0.15
ball_y_change = 0.15

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0, Player B: 0", align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()


def paddle_a_up():
    if paddle_a.ycor() < 300:
        y = paddle_a.ycor()
        y = y + 20
        paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() > -300:
        y = paddle_a.ycor()
        y = y - 20
        paddle_a.sety(y)


def paddle_b_up():
    if paddle_b.ycor() < 300:
        y = paddle_b.ycor()
        y = y + 20
        paddle_b.sety(y)


def paddle_b_down():
    if paddle_b.ycor() > -300:
        y = paddle_b.ycor()
        y = y - 20
        paddle_b.sety(y)


turtle.onkeypress(paddle_a_up, 'w')
turtle.onkeypress(paddle_a_down, 's')
turtle.onkeypress(paddle_b_up, 'Up')
turtle.onkeypress(paddle_b_down, 'Down')
turtle.listen()

score_a = 0
score_b = 0

while True:
    window.update()

    # moving ball
    ball.setx(ball.xcor() + ball_x_change)
    ball.sety(ball.ycor() + ball_y_change)

    # border checking: top, bottom
    if ball.ycor() > 290 or ball.ycor() < -290:
        # ball_y_change = ball_y_change * -1
        ball_y_change *= -1

    # border checking: right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_x_change *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    # border checking: left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_x_change *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    # paddle and ball bouncing
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 60 < ball.ycor() < paddle_b.ycor() + 60):
        ball.setx(340)
        ball_x_change *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 60 < ball.ycor() < paddle_a.ycor() + 60):
        ball.setx(-340)
        ball_x_change *= -1
