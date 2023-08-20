import turtle
import random


window = turtle.Screen()
window.setup(800, 800)
window.bgcolor('black')

t = turtle.Turtle()
t.speed(0)
colors = ['red', 'green', 'hot pink', 'orange red']


def draw_firework():
    t.color(random.choice(colors))

    size = random.randint(50, 150)

    # give random integer from [-400, 400]
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    t.penup()
    t.goto(x, y)
    t.pendown()

    for i in range(36):
        t.forward(size)
        t.backward(size)
        t.right(10)


for i in range(10):
    draw_firework()


t.penup()
t.goto(0, 100)
t.color('white')
t.write('Happy new year!', align='center', font=('Verdana', 24, 'normal'))

turtle.done()
