'''
list
tuple
dictionary
set

def

class + pygame

ccc J3, J4
'''
import turtle
import random

screen = turtle.Screen()
screen.bgcolor('lightblue')
screen.setup(600, 600)

score = 0
time_left = 30

t = turtle.Turtle()
t.shape('turtle')
t.penup()

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 200)
score_display.write("Score: 0", align="center", font=("Arial", 18, "bold"))

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

def move_turtle(x=None, y=None):
    global score
    if x is not None and y is not None:
        score += 1
        update_score()
    pos = random.choice(list(positions.values()))
    t.goto(pos)

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
        move_turtle()
        screen.ontimer(auto_move, 1000)


t.onclick(move_turtle)
countdown()
auto_move()
move_turtle()
screen.mainloop()
