'''
1. continue on Python programming knowledge
-
2. CCC
'''
import time
import turtle
import random


screen = turtle.Screen()
screen.title("Click the Turtle Game")
screen.bgcolor("lightblue")
screen.setup(600, 600)

score = 0
time_left = 60

mole = turtle.Turtle()
mole.shape('turtle')
mole.penup()

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 200)
score_display.write("Score: 0", align="center", font=("Arial", 18, "bold"))

time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.goto(0, 170)
time_display.write("Time: " + str(time_left), align="center", font=("Arial", 16, "normal"))

positions = [(-200, 150), (-100, 50), (0, 100), (100, -50),
             (200, 0), (-150, -100), (150, 150), (0, -150)
             ]

mole.goto(random.choice(positions))

start_time = time.time()
last_move = time.time()

def clicked(x, y):
    global score, last_move
    score += 1
    score_display.clear()
    score_display.write("Score: " + str(score), align="center", font=("Arial", 18, "bold"))
    mole.goto(random.choice(positions))
    screen.update()
    last_move = time.time()

mole.onclick(clicked)

while time_left > 0:
    # the mole is not clicked within 1s
    if time.time() - last_move >= 1:
        mole.goto(random.choice(positions))
        last_move = time.time()

screen.mainloop()


'''
Given a nested list [[1,2,3],[4,5,6],[7,8,9]], flatten it into [1,2,3,4,5,6,7,8,9]

'''