import turtle
import random


wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setup(800, 600)
wn.tracer(0)

turtle_properties = {
    'turtle1': {'color': 'red', 'shape': 'turtle', 'speed': 1},
    "turtle2": {"color": "green", "shape": "turtle", "speed": 2},
    "turtle3": {"color": "blue", "shape": "turtle", "speed": 3},
    "turtle4": {"color": "yellow", "shape": "turtle", "speed": 4},
    "turtle5": {"color": "purple", "shape": "turtle", "speed": 5}
}

turtles = {}

for name, props in turtle_properties.items():
    t = turtle.Turtle()
    t.color(props['color'])
    t.shape(props['shape'])
    t.penup()
    t.speed(0)
    t.goto(random.randint(-380, 380), random.randint(-280, 280))
    turtles[name] = t

def move_turtles():
    for name, t in turtles.items():
        t.forward(turtle_properties[name]['speed'])
        turn_angle = random.randint(0, 10)

        if random.choice(['left', 'right']) == 'left':
            t.left(turn_angle)
        else:
            t.right(turn_angle)

        if t.xcor() > 390 or t.xcor() < -390:
            t.right(180)
        if t.ycor() > 290 or t.ycor() < -290:
            t.right(180)

        for another_name, another_t in turtles.items():
            if another_name != name and t.distance(another_t) < 20:
                t.right(180)
                another_t.right(180)
    wn.update()
    wn.ontimer(move_turtles, 20)

move_turtles()
wn.mainloop()