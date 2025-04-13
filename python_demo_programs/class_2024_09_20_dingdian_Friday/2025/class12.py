import turtle
import random


screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('lightblue')

t = turtle.Turtle()
t.shape('turtle')
t.color('green')
t.penup()

t1 = turtle.Turtle()
t1.shape('turtle')
t1.color('yellow')
t1.penup()
t1.goto(random.randint(-200, 200), random.randint(-200, 200))

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 250)
score = 0

pen.write('Score: ' + str(score), align='center', font=('Arial', 24, 'bold'))

def move(x, y):
    global score
    score += 1
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    pen.clear()
    pen.write('Score: ' + str(score), align='center', font=('Arial', 24, 'bold'))


def move_t1(x, y):
    global score
    score += 1
    t1.goto(random.randint(-200, 200), random.randint(-200, 200))
    pen.clear()
    pen.write('Score: ' + str(score), align='center', font=('Arial', 24, 'bold'))


t.goto(0, 0)
t.onclick(move)
t1.onclick(move_t1)
turtle.done()