import turtle
import random

window = turtle.Screen()
window.setup(800, 800)
window.bgcolor('black')

pen = turtle.Turtle()
pen.speed(0)
colors = ['yellow', 'red', 'green', 'orange', 'blue']

def draw_firework():
    size = random.randint(50, 150)
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    pen.color(random.choice(colors))
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # for i in range(36):
    #     pen.forward(size)
    #     pen.backward(size)
    #     pen.right(10)
    for i in range(20):
        pen.circle(size)
        pen.right(18)

for i in range(10):
    draw_firework()

turtle.done()
