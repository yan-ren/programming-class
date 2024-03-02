'''
list = []
list.append(1)
print(list)
list.append(2)
print(list)

print(list[0])
list[0] = 100
print(list)

list = [1, 2, 3, 4, 5, 6]
index = len(list) - 1
while index >= 0:
    print(list[index])
    index -= 1

del list[4]
print(list)
'''
import turtle

wn = turtle.Screen()
wn.setup(800, 600)
wn.tracer(0)
wn.bgcolor('black')

# left paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.shapesize(5, 1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Right paddle
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.color('white')
paddle_right.penup()
paddle_right.goto(350, 0)
paddle_right.shapesize(5, 1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.dx = 0.02
ball.dy = 0.02

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write('Player A: 0, Player B: 0', align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()


def left_paddle_up():
    y = paddle_left.ycor()
    y = y + 20
    paddle_left.sety(y)


def left_paddle_down():
    y = paddle_left.ycor()
    y = y - 20
    paddle_left.sety(y)


def right_paddle_up():
    paddle_right.sety(paddle_right.ycor() + 20)


def right_paddle_down():
    paddle_right.sety(paddle_right.ycor() - 20)


wn.onkeypress(left_paddle_up, 'w')
wn.onkeypress(left_paddle_down, 's')
wn.onkeypress(right_paddle_up, 'Up')
wn.onkeypress(right_paddle_down, 'Down')
wn.listen()

# score
paddle_right_score = 0
paddle_left_score = 0

while True:
    wn.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # right border
    if ball.xcor() > 390:
        ball.dx *= -1
        paddle_left_score += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(paddle_left_score, paddle_right_score), align='center', font=('Courier', 24, 'bold'))

    # left border
    if ball.xcor() < -390:
        ball.dx *= -1
        paddle_right_score += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(paddle_left_score, paddle_right_score), align='center', font=('Courier', 24, 'bold'))

    # left paddle
    if ball.xcor() < paddle_left.xcor() and paddle_left.ycor() - 60 < ball.ycor() < paddle_left.ycor() + 60:
        ball.dx = -ball.dx
    # right paddle
    if ball.xcor() > paddle_right.xcor() and paddle_right.ycor() - 60 < ball.ycor() < paddle_right.ycor() + 60:
        ball.dx = -ball.dx