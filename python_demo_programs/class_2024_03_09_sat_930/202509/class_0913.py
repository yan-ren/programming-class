'''
list
dictionary
tuple
set

def

class

'''

import turtle
import random
import time


screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('lightblue')

score = 0
time_left = 30

# turtle to click
t = turtle.Turtle()
t.shape('turtle')
t.penup()

# score display
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 200)
score_display.write("Score: 0", align="center", font=("Arial", 18, "bold"))

# timer display
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(0, 170)
timer_display.write("Time: 30", align="center", font=("Arial", 16, "normal"))

positions = {
    1: (-200, 150),
    2: (-100, 50),
    3: (0, 100),
    4: (100, -50),
    5: (200, 0),
    6: (-150, -100),
    7: (150, 150),
    8: (0, -150)
}

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))


def update_timer():
    timer_display.clear()
    timer_display.write(f"Time: {time_left}", align="center", font=("Arial", 16, "normal"))

last_click_time = time.time()

def move_turtle(x=None, y=None):
    global score, last_click_time
    if x is not None and y is not None: # means user clicked
        score += 1
        update_score()
    t.goto(random.choice(list(positions.values())))
    last_click_time = time.time()

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        update_timer()
        screen.ontimer(countdown, 1000)
    else:
        t.hideturtle()
        score_display.goto(0, 0)
        score_display.write(f"Game Over!\nFinal Score: {score}", align="center", font=("Arial", 20, "bold"))

def auto_move():
    if time_left > 0:
        if time.time() - last_click_time >= 0.5:
            move_turtle()
        screen.ontimer(auto_move, 100)

t.onclick(move_turtle)
countdown()
auto_move()
t.goto(random.choice(list(positions.values())))
screen.mainloop()


