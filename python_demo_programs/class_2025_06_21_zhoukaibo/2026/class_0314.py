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
score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

def update_score():
    score_turtle.clear()
    score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

targets = []
def create_target():
    target = turtle.Turtle()
    target.shape('circle')
    target.color('red')
    target.penup()
    target.speed(0)
    targets.append(target)
    return target

def move_target(target):
    target.goto(random.randint(-390, 390), random.randint(-290, 290))
    wn.ontimer(lambda: move_target(target), 3000)

def click_target(x, y, target):
    global score
    if target.pencolor() == 'red':
        score += 1
    update_score()
    move_target(target)

def bind_click_event(target):
    target.onclick(lambda x, y: click_target(x, y, target))
    
def setup_targets():
    for _ in range(5):
        target = create_target()
        move_target(target)
        bind_click_event(target)

setup_targets()
wn.mainloop()
