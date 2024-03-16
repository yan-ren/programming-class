# def greeting():
#     print("welcome to the class")
#     print("have a wonderful day")
#
#
# def math(a, b):
#     greeting()
#     return a + b, a * b
#
#
# greeting()
# add, mul = math(1, 2)
# print(add)
# print(mul)
import random
# def method1():
#     print('in method1')
#
#
# def method2(a, b):
#     if a > b:
#         method1()
#     else:
#         print('in method2')
#
#
# def method3(a, b):
#     method2(b, a)
#     print('in method3')
#
#
# method3(1, 2)
# method3(2, 1)

import turtle
import random

# create 800x800 screen
window = turtle.Screen()
window.setup(800, 800)
window.bgcolor('black')

# create turtle object
t = turtle.Turtle()
t.penup()
t.speed(0)

def draw_firework():
    colors = ['red', 'green', 'hot pink', 'orange red']
    t.color(random.choice(colors))
    size = random.randint(50, 150)
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    t.penup()
    t.goto(x, y)
    t.pendown()

    # draw firework
    for i in range(36):
        t.forward(size)
        t.backward(size)
        t.right(10)


for i in range(10):
    draw_firework()


turtle.done()

