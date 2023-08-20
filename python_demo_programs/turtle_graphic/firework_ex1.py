import turtle
import random


window = turtle.Screen()
window.setup(600, 600)

window.bgcolor('black')

# create turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
colors = ['blue', 'yellow']


def draw_firework():
    # make turtle go to the random place
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.goto(x, y)
    t.pendown()
    size = random.randint(50, 150)

    t.color(random.choice(colors))
    # draw firework
    for i in range(36):
        t.forward(size)
        t.backward(size)
        t.left(10)


for i in range(10):
    draw_firework()


t.penup()
t.goto(0, 100)
t.color('white')
t.write('Happy new year!', align='center', font=('Verdana', 24, 'normal'))

turtle.done()

