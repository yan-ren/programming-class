'''
Exercise1:

create a list of colors and use random to pickup the color for turtle

draw some pattern using loops and the previous selected random color
'''
import turtle
import random

screen = turtle.Screen()
screen.setup(600, 800)

t = turtle.Turtle()

def draw_heart(t, size):
    t.fillcolor(random.choice(['red', 'pink', 'purple', 'orange']))
    t.begin_fill()
    t.left(140)
    t.forward(size)
    t.circle(-size/2, 200)
    t.left(120)
    t.circle(-size/2, 200)
    t.forward(size)
    t.end_fill()


for _ in range(10):
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    t.pendown()
    t.setheading(random.randint(180, 360))
    size = random.randint(50, 150)
    draw_heart(t, size)

turtle.done()