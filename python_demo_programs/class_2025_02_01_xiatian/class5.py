# import random
#
# # looping
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1
#
# color = random.choice(['red', 'yellow', 'blue'])
#

'''
use turtle, create a count down program
'''
import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor('white')

counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(0, 0)

timer = 10

while timer >= 0:
    # show this timer value on screen
    screen.clear()
    screen.bgcolor(random.choice(["white", "lightblue", "lightgreen", "yellow", "pink"]))

    font_size = 48 + (timer % 2) * 10  # Alternates between 48 and 58
    counter.write(timer, align="center", font=("Arial", font_size, "bold"))

    timer -= 1
    time.sleep(1)

for _ in range(6):
    screen.bgcolor(random.choice(["red", "orange", "purple", "blue"]))
    counter.write("Time's up!", align="center", font=("Arial", 48, "bold"))
    time.sleep(0.5)
    screen.clear()
    time.sleep(0.5)

counter.write("Time's up!", align="center", font=("Arial", 48, "bold"))

turtle.done()
