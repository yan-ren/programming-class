from turtle import *
import time
import random


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.bgpic('border.gif')
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

while True:
    time.sleep(0.01)
    screen.update()
    move_snake()

    # border checking
    if head.xcor() > 260 or head.xcor() < -260 or head.ycor() > 260 or head.ycor() < -260:
        text.clear()
        text.write('Game Lost',align='center',font=('courier',34,'bold'))
        break

done()