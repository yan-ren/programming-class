'''more about return'''
'''
return keyword:
1. return a value to where the function being called
2. terminate the function
'''
def find_max(list):
    if len(list) == 0:
        return

    max_value = list[0]

    for value in list:
        if value > max_value:
            max_value = value

    return max_value


def find_min_max(list):
    if len(list) == 0:
        return

    max_value = list[0]
    min_value = list[0]

    for value in list:
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value

    return min_value, max_value


# a, b = find_min_max([1, 2, 3, 4, 5])
# print(a)
# print(b)

import turtle


wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(800, 600)
wn.tracer(0)

# Left paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.shapesize(5, 1)
paddle_left.color('white')
paddle_left.penup()
paddle_left.goto(-390, 0)

# Right paddle
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(5, 1)
paddle_right.color('white')
paddle_right.penup()
paddle_right.goto(390, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.xchange = 0.05
ball.ychange = 0.05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()

def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

while True:
    wn.update()