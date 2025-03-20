import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setup(800, 600)

score = 0
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color('black')
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 260)
score_turtle.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

targets = []
colors = ['red', 'yellow', 'blue']

def create_target():
    target = turtle.Turtle()
    target.shape("circle")
    target.color(random.choice(colors))
    target.penup()
    target.speed(0)
    targets.append(target)
    return target

def move_target(target):
    target.goto(random.randint(-390, 390), random.randint(-290, 290))
    wn.ontimer(lambda: move_target(target), 3000)

def update_score():
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def click_target(x, y, target):
    global score
    color = target.color()[0]
    if color == 'red':
        score += 1
    elif color == 'yellow':
        score += 2
    elif color == 'blue':
        score += 3
    target.color(random.choice(colors))
    update_score()
    move_target(target)

def bind_click_event(target):
    target.onclick(lambda x, y: click_target(x, y, target))

def start():
    for _ in range(5):
        target = create_target()
        move_target(target)
        bind_click_event(target)

start()
wn.mainloop()

'''
let dot can only choose color randomly from 'red' 'yellow' 'blue'
and when click red +1 score, click yellow +2 score, click blue +3 score
'''