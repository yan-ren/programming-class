'''
Data structure: Dictionary

real life dictionary: word - sentence
programming dictionary: key - value
'''

# d = {}
# d['one'] = 1
# d['two'] = 2
#
# print(d)
# print(d['one'])
#
# if 'one' in d:
#     print('one exists')
#
# del d['one']
#
# d = {'a': 1, 'b': 2, 'c': 3}
# d['a'] = 100
# print(d)
# # loop dictionary by key
# for k in d.keys():
#     print(k, d[k])
# # loop dictionary by value
# for v in d.values():
#     print(v)
#
# for k, v in d.items():
#     print(k, v)
#
# import turtle
#
# screen = turtle.Screen()
# screen.colormode(255)

# shapes = {
#     "circle1": {"color": (255, 0, 0), "position": (-100, 100), "size": 2},
#     "circle2": {"color": (0, 255, 0), "position": (0, 0), "size": 3},
#     "circle3": {"color": (0, 0, 255), "position": (100, -100), "size": 1.5}
# }
#
# for name, info in shapes.items():
#     t = turtle.Turtle()
#     t.shape('circle')
#     t.penup()
#     t.goto(info['position'])
#     t.color(info['color'])
#     t.shapesize(info['size'])
#     t.stamp()
#
# turtle.done()

import turtle
import random

screen = turtle.Screen()
screen.bgcolor('black')
turtle.colormode(255)
screen.setup(800, 600)
screen.tracer(0)

turtles = {
    "red": {
        "turtle": turtle.Turtle(),
        "color": (255, 50, 50),
        "position": (-200, 0),
        "shape": "turtle",
        "speed": 3,
        "direction": random.randint(0, 360),
        "step": 3
    },
    "green": {
        "turtle": turtle.Turtle(),
        "color": (50, 255, 50),
        "position": (0, 0),
        "shape": "circle",
        "speed": 2,
        "direction": random.randint(0, 360),
        "step": 5
    }
}

for data in turtles.values():
    t = data['turtle']
    t.shape(data['shape'])
    t.color(data['color'])
    t.penup()
    t.goto(data['position'])
    t.setheading(data['direction'])
    t.speed(0)

def move_turtles():
    for data in turtles.values():
        t = data['turtle']
        t.forward(data['step'])
        t.left(random.randint(-10, 10))
        x, y = t.xcor(), t.ycor()
        if abs(x) > 390 or abs(y) > 290:
            t.setheading(t.heading() + 180)

    screen.update()
    screen.ontimer(move_turtles, 50)

move_turtles()
screen.mainloop()