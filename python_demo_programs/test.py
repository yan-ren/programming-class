import turtle
import random


wn = turtle.Screen()
wn.bgcolor('lightblue')
WIDTH = 800
HEIGHT = 600
wn.setup(WIDTH, HEIGHT)

dots = []
current_score = 0

score = turtle.Turtle()
score.hideturtle()
score.penup()
score.color('black')
score.goto(0, 260)
score.write('Score:' + str(current_score), font=('Courier', 24, 'normal'))

def create_dot():
    dot = turtle.Turtle()
    dot.shape('circle')
    color = ('tomato', 'deep sky blue', 'green',)
    dot.color(random.choice(color))
    dot.penup()
    dot.speed(0)
    return dot


def move_dot(dot):
    dot.goto(random.randint(-WIDTH//3, WIDTH//3), random.randint(-HEIGHT//3, HEIGHT/3))
    wn.ontimer(lambda: move_dot(dot), 3000)


def when_click(dot):
    global current_score
    dot.goto(random.randint(-WIDTH//3, WIDTH//3), random.randint(-HEIGHT//3, HEIGHT//3))

    if dot.pencolor() == 'tomato':
        current_score += 1
        score.clear()
        score.write('Score:' + str(current_score), font=('Courier', 24, 'normal'))
    if dot.pencolor() == 'deep sky blue':
        current_score -= 1
        score.clear()
        score.write('Score:' + str(current_score), font=('Courier', 24, 'normal'))
    if dot.pencolor() == 'green':
        current_score -= 2
        score.clear()
        score.write('Score:' + str(current_score), font=('Courier', 24, 'normal'))

def handle_click(dot):
    dot.onclick(lambda x, y: when_click(dot))

for i in range(5):
    dots.append(create_dot())

for dot in dots:
    move_dot(dot)

for dot in dots:
    handle_click(dot)

turtle.done()