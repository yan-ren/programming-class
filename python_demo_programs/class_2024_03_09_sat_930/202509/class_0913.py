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

# def move_turtle(x, y):


# def countdown():



