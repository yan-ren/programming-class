from turtle import *
import time
import random


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.bgpic('border.gif')
screen.tracer(False)
register_shape('upmouth.gif')
register_shape('food.gif')
register_shape('downmouth.gif')
register_shape('leftmouth.gif')
register_shape('rightmouth.gif')
register_shape('body.gif')

head = Turtle()
head.shape('upmouth.gif')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

food = Turtle()
food.shape('food.gif')
food.penup()
food.goto(0, 100)

text = Turtle()
text.color('white')
text.penup()
text.hideturtle()

def go_up():
    head.direction = 'up'
    head.shape('upmouth.gif')

def go_down():
    head.direction = 'down'
    head.shape('downmouth.gif')

def go_left():
    head.direction = 'left'
    head.shape('leftmouth.gif')

def go_right():
    head.direction = 'right'
    head.shape('rightmouth.gif')

def move_snake():
    if head.direction == 'up':
        head.sety(head.ycor() + 20)
    if head.direction == 'down':
        head.sety(head.ycor() - 20)
    if head.direction == 'right':
        head.setx(head.xcor() + 20)
    if head.direction == 'left':
        head.setx(head.xcor() - 20)


screen.listen()
screen.onkeypress(go_up, 'Up')
screen.onkeypress(go_down, 'Down')
screen.onkeypress(go_left, 'Left')
screen.onkeypress(go_right, 'Right')
segments = []
execution_delay = 0.1

while True:
    screen.update()

    # border checking
    if head.xcor() > 260 or head.xcor() < -260 or head.ycor() > 260 or head.ycor() < -260:
        text.clear()
        text.write('Game Lost', align='center',font=('courier',34,'bold'))
        break

    if head.distance(food) < 20:
        food.goto(random.randint(-250, 250), random.randint(-250, 250))

        execution_delay = execution_delay - 0.003
        body = Turtle()
        body.penup()
        body.shape('body.gif')
        segments.append(body)

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move_snake()

    # check head runs into the body
    for body in segments:
        if body.distance(head) < 20:
            text.clear()
            text.write('Game Lost', align='center', font=('courier', 34, 'bold'))

    time.sleep(execution_delay)

done()
