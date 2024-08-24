import random
import time
import turtle


wn = turtle.Screen()
wn.setup(600, 600)
wn.bgcolor('black')
wn.bgpic('border.gif')
wn.tracer(False)

turtle.register_shape('upmouth.gif')
turtle.register_shape('food.gif')
turtle.register_shape('downmouth.gif')
turtle.register_shape('leftmouth.gif')
turtle.register_shape('rightmouth.gif')
turtle.register_shape('body.gif')

head = turtle.Turtle()
head.shape('upmouth.gif')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

food = turtle.Turtle()
food.shape('food.gif')
food.penup()
food.goto(0, 100)

text = turtle.Turtle()
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


wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')
wn.listen()

def move_snake():
    if head.direction == 'up':
        head.sety(head.ycor() + 10)
    if head.direction == 'down':
        head.sety(head.ycor() - 10)
    if head.direction == 'right':
        head.setx(head.xcor() + 10)
    if head.direction == 'left':
        head.setx(head.xcor() - 10)


segments = []
score = 0

while True:
    wn.update()
    move_snake()

    # border checking
    if head.xcor() > 260 or head.xcor() < -260 or head.ycor() > 260 or head.ycor() < -260:
        text.clear()
        text.write('Game Lost', align='center', font=('courier', 34, 'bold'))
        break

    if head.distance(food) < 20:
        food.goto(random.randint(-250, 250), random.randint(-250, 250))
        score += 1
        text.clear()
        text.write('Score: ' + str(score), font = ('courier', 25, 'bold'), align='center')


    time.sleep(0.05)


turtle.done()
