import turtle

wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(800, 600)
wn.tracer(0)

left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape('square')
left_paddle.color('white')
left_paddle.penup()
left_paddle.goto(-350, 0)
left_paddle.shapesize(5, 1)

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.penup()
right_paddle.goto(350, 0)
right_paddle.shapesize(5, 1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 0.5
ball.dy = 0.5

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write('Player A: 0 Player B: 0', align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()

score_a = 0
score_b = 0

def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

wn.listen()
wn.onkeypress(left_paddle_up, 'w')
wn.onkeypress(left_paddle_down, 's')
wn.onkeypress(right_paddle_up, 'Up')
wn.onkeypress(right_paddle_down, 'Down')

while True:
    wn.update()