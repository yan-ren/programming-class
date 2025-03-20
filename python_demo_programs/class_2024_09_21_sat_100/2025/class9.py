import time
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
score_turtle.goto(0, 250)
score_turtle.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

targets = []
colors = ['red', 'yellow', 'green']

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
    move_target(target)
    color = target.color()[0]
    if color == 'red':
        score += 1

    update_score()

def bind_click(target):
    target.onclick(lambda x, y: click_target(x, y, target))

def start():
    for _ in range(5):
        target = create_target()
        move_target(target)
        bind_click(target)

start()
wn.mainloop()

'''
More features to consider
1. add more dots, some dots may lead to point deduction
2. add timer and game finish condition. e.g. when people get 10 scores, finish the game
and should how much time to get 10 scores
time.time()
'''
