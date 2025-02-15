'''
firework
'''
import turtle
import random
from pkgutil import resolve_name

window = turtle.Screen()
window.setup(800, 600)
window.bgcolor('black')

t = turtle.Turtle()
t.speed(0)
colors = ['red', 'green', 'hot pink', 'orange red']

pen = turtle.Turtle()
pen.penup()
pen.speed(0)

j = 0
while j < 10:
    t.color(random.choice(colors))
    size = random.randint(50, 150)

    # give random integer for location from x = [-400, 400], y = [0. 300]
    x = random.randint(-400, 400)
    y = random.randint(0, 300)
    t.penup()
    t.goto(x, y)
    t.pendown()

    for i in range(36):
        # t.forward(size)
        # t.backward(size)
        t.circle(size // 4)
        t.right(10)

    j += 1


pen.write('Happy New Year', align='center', font=('Verdana', 24, 'normal'))
turtle.done()

'''
challenge 1: how to draw multiple firework, hint: using for loop/while loop
challenge 2: design your own firework shape
'''