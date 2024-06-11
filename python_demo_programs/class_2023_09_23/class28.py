# d = {'name': 'Tom', 'age': 9}
#
# print(d['name'])
import time
import turtle
import random

# Setup the screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turn off automatic screen updates

# dictionary to store each turtle properties
turtle_properties = {
    "turtle1": {"color": "red", "speed": 1},
    "turtle2": {"color": "green", "speed": 2},
    "turtle3": {"color": "blue", "speed": 3},
    "turtle4": {"color": "yellow", "speed": 4},
    "turtle5": {"color": "purple", "speed": 5}
}

turtles = {}
# loop through the dictionary to create turtle
# loop ke and value at the same time
for key, value in turtle_properties.items():
    t = turtle.Turtle()
    t.color(value['color'])
    t.shape('turtle')
    t.penup()
    t.goto(random.randint(-380, 380), random.randint(-280, 280))
    turtles[key] = t


# create the player turtle
player = turtle.Turtle()
player.shape('turtle')
player.color('black')
player.penup()
player.speed(0)
player.goto(0, -290)

move_up_active = False
move_down_active = False

def start_move_up():
    global move_up_active
    move_up_active = True

def stop_move_up():
    global move_up_active
    move_up_active = False

def start_move_down():
    global move_down_active
    move_down_active = True

def stop_move_down():
    global move_down_active
    move_down_active = False

wn.listen()
wn.onkeypress(start_move_up, 'Up')
wn.onkeyrelease(stop_move_up, 'Up')
wn.onkeypress(start_move_down, 'Down')
wn.onkeyrelease(stop_move_down, 'Down')

# make turtle move in given speed
while True:
    wn.update()
    time.sleep(0.01)

    for name, t in turtles.items():
        t.forward(turtle_properties[name]['speed'])
        # bounce back if the turtle hits the screen edge
        if t.xcor() > 390 or t.xcor() < -390:
            t.right(180)

    # check for collision with the player
    for name, t in turtles.items():
        if t.distance(player) < 20:
            player.goto(0, -290)

turtle.done()