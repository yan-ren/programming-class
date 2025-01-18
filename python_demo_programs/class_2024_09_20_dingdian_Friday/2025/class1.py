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


turtle.done()
