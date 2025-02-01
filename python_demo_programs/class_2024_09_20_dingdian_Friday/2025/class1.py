import turtle

wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor('black')
wn.tracer(0)

paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.penup()
paddle_left.goto(-350, 0)
paddle_left.shapesize(5, 1)

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.color('white')
paddle_right.penup()
paddle_right.goto(350, 0)
paddle_right.shapesize(5, 1)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.speed(0)
ball.dx = 0.01
ball.dy = 0.01

left_score = 0
right_score = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('white')
pen.speed(0)
pen.goto(0, 260)
pen.write('Player A: {} Player B: {}'.format(left_score, right_score), align='center', font=('Courier', 24, 'bold'))

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)


wn.listen()
wn.onkeypress(paddle_left_up, 'w')
wn.onkeypress(paddle_left_down, 's')
wn.onkeypress(paddle_right_up, 'Up')
wn.onkeypress(paddle_right_down, 'Down')

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy = -ball.dy

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx = -ball.dx

    if ball.xcor() < paddle_left.xcor() + 5 and paddle_left.ycor() - 60 < ball.ycor() < paddle_left.ycor() + 60:
        ball.dx = -ball.dx

    if ball.xcor() > paddle_right.xcor() + 5 and paddle_right.ycor() - 60 < ball.ycor() < paddle_right.ycor() + 60:
        ball.dx = -ball.dx

    if ball.xcor() > 390:
        left_score += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(left_score, right_score), align='center',
                  font=('Courier', 24, 'bold'))

    if ball.xcor() < -390:
        right_score += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(left_score, right_score), align='center',
                  font=('Courier', 24, 'bold'))
        
turtle.done()
