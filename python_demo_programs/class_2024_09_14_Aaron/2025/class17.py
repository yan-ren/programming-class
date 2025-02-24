import random
import time
import turtle

screen = turtle.Screen()
screen.setup(600, 800)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

def draw_die(x, y, value):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    # draw square
    for _ in range(4):
        drawer.forward(50)
        drawer.right(90)

    # write number in the center
    drawer.penup()
    drawer.goto(x + 20, y - 35)
    drawer.write(value, align='center', font=("Arial", 20, "bold"))

d1 = [1, 2, 3, 4, 5, 6]
d2 = [1, 2, 3, 4, 5, 6]

def roll_dice(x, y):
    for _ in range(3):
        v1 = random.choice(d1)
        v2 = random.choice(d2)

        drawer.clear()
        draw_die(-60, 60, v1)
        draw_die(10, 60, v2)
        time.sleep(3)


screen.onclick(roll_dice)
turtle.done()


'''
use turtle, create a count down program
'''