import turtle
import random


wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setup()

def create_dot():
    dot = turtle.Turtle()
    dot.shape('circle')
    dot.color('red')
    dot.penup()
    dot.speed(0)
    return dot


def move_dot(d):
    d.goto(random.randint(-390, 390), random.randint(-290, 290))
    # move the dot every 3 seconds
    wn.ontimer(lambda: move_dot(d), 3000)


score = 0

score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color('black')
score_turtle.penup()
score_turtle.goto(0, 260)
score_turtle.write('Score:' + str(score), font=('Courier', 24, 'normal'))
score_turtle.hideturtle()

def draw_score():
    score_turtle.clear()
    score_turtle.write('Score:' + str(score), font=('Courier', 24, 'normal'))

def when_click(dot):
    global score
    score += 1
    # move_dot(dot)
    dot.goto(random.randint(-390, 390), random.randint(-290, 290))
    draw_score()

def handle_click(dot):
    dot.onclick(lambda x, y: when_click(dot))

dots = []

for i in range(5):
    dots.append(create_dot())

for d in dots:
    move_dot(d)

for d in dots:
    handle_click(d)

turtle.done()