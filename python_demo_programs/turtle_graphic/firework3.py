import turtle
import random
import time

# set screen size
win = turtle.Screen()
win.screensize(600, 600)

# set turtle for firework
start = turtle.Turtle()
# set turtles for burst
burst1 = turtle.Turtle()

burst1.hideturtle()
colors = ["#FFFFFF", "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#C0C0C0", "#808080", "#800000",
          "#808000", "#008000", "#800080", "#008080", "#000080"]


def base():
    start.ht()
    start.pencolor("White")
    start.speed(0)
    start.up()
    start.goto(random.randint(-100, 100), -300)
    start.down()
    start.setheading(90)
    start.pensize(3)
    for x in range(random.randint(5, 45)):
        start.forward(10)
        start.up()
        start.forward(10)
        start.down()
        start.clear()


# burst
def burst():
    head = 15
    burst1.speed(0)
    burst1.pensize(3)
    for x in range(25):
        turtle.tracer(0, 0)
        burst1.ht()
        burst1.up()
        burst1.goto(start.xcor(), start.ycor())
        burst1.down()
        burst1.setheading(head)
        for x in range(5):
            burst1.color(random.choice(colors))
            burst1.forward(random.randint(3, 15))
            burst1.up()
            burst1.forward(random.randint(3, 15))
            burst1.down()
            head = head + 15
            turtle.update()


# reset
while True:
    win.bgcolor("black")
    base()
    burst()
    turtle.clearscreen()