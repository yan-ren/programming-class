'''
2015-2012 J2, you can find questions on dmoj

https://cemc.uwaterloo.ca/sites/default/files/documents/2015/2015CCCJrProblems.html
https://cemc.uwaterloo.ca/sites/default/files/documents/2014/2014CCCJrProblems.html
https://mmhs.ca/ccc/2013/ccc2013Junior.pdf
http://darcy.rsgc.on.ca/ACES/ICS3U/CCC/juniorEn2012.pdf

2018, 2017 J3, think and try the solution
'''
import time
import turtle
import random

window = turtle.Screen()
window.setup(800, 800)
window.bgcolor('black')
window.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
colors = ['red', 'green', 'hot pink', 'orange red', 'gold']

def draw_tail(x, start_y, end_y, color):
    pen.color(color)
    pen.pensize(3)

    tail_length = 30
    y = start_y

    while y < end_y:
        pen.clear()
        pen.penup()
        tail_start = max(start_y, y - tail_length)
        pen.goto(x, tail_start)
        pen.pendown()
        pen.goto(x, y)
        pen.penup()
        pen.goto(x, y)
        pen.dot(6, 'white')
        y += 15
        window.update()

    pen.clear()
    pen.pensize(1)

def draw_firework():
    color = random.choice(colors)
    size = random.randint(50, 120)
    x = random.randint(-400, 400)
    y = random.randint(-100, 400)

    draw_tail(x, -400, y, color)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    for i in range(20):
        pen.circle(size)
        pen.right(18)
        window.update()

    time.sleep(0.3)
    pen.clear()

for i in range(10):
    draw_firework()

pen.clear()
pen.penup()
pen.goto(0, 100)
pen.write('Happy new year!', align='center', font=('Verdana', 24, 'normal'))

turtle.done()