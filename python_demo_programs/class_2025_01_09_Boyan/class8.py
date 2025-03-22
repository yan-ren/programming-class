import turtle
import time
import random
import tkinter
import _tkinter

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('lightblue')

counter = turtle.Turtle()
counter.hideturtle()
counter.penup()

# count down
screen.tracer(0) # turn off the screen auto update
start = int(screen.textinput('Enter a number for count down', 'Enter a number for count down'))

while start >= 0:
    counter.clear()
    screen.clear()
    screen.bgcolor(random.choice(['white', 'lightblue', 'lightgreen', 'yellow', 'pink']))
    counter.write(start, align='center', font=('Arial', 48, 'bold'))
    screen.update()
    start -= 1
    time.sleep(1)


# finish message
#

turtle.done()
