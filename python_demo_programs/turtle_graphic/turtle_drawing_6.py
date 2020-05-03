import turtle
import random

wn = turtle.Screen()
tess = turtle.Turtle()
tess.speed(10)

wn.colormode(255)
for n in range(60):
    tess.penup()
    tess.goto(random.randint(-400, 400), random.randint(-400, 400))
    tess.pendown()

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    tess.pencolor((red, green, blue))

    circle_size = random.randint(10, 40)
    tess.pensize(random.randint(1, 5))

    for i in range(6):
        tess.circle(circle_size)
        tess.left(60)