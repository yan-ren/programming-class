import turtle
import random


window = turtle.Screen()
window.setup(800, 800)
window.bgcolor('black')

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
colors = ['red', 'green', 'yellow']

def draw_firework():
    pen.clear()
    pen.color(random.choice(colors))
    size = random.randint(100, 150)
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    for i in range(20):
        pen.forward(size)
        pen.backward(size)
        pen.right(18)

for i in range(10):
    draw_firework()

pen.penup()
pen.goto(0, 100)
pen.color('white')
pen.write('Happy New Year!', align='center', font=('Verdana', 24, 'normal'))

turtle.done()
