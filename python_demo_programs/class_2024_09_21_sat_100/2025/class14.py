'''
List
Tuple
Dictionary
Set
'''

'''
Today:

Build project using data structure, try to use images in project
'''

import turtle
import random

screen = turtle.Screen()
screen.setup(1200, 800)
screen.bgcolor('lightblue')

# make sure images are in the same folder
screen.addshape('rose.gif')
screen.addshape('ladybug.gif')

colors = ['red', 'blue', 'green', 'yellow', 'purple']
positions = [(-150, 150), (0, 150), (150, 150),
             (-150, 0), (0, 0), (150, 0),
             (-150, -150), (0, -150), (150, -150)]

# hold all turtle objects
all_turtles = []
turtle_data = {}

# create turtles
index = 0
for pos in positions:
    t = turtle.Turtle()
    t.penup()
    t.goto(pos)

    chosen_color = random.choice(colors)
    chosen_shape = random.choice(["rose.gif", "ladybug.gif"])

    t.shape(chosen_shape)
    t.color(chosen_color)
    t.speed(random.randint(1, 10))

    all_turtles.append(t)
    turtle_data[index] = {
        'color': chosen_color,
        'position': pos,
        'shape': chosen_shape,
        'speed': t.speed()
    }

    index += 1

def move_turtles():
    for t in all_turtles:
        angle = random.randint(0, 360)
        distance = random.randint(20, 50)
        t.right(angle)
        t.forward(distance)

# print turtle info when clicked it
def show_turtle_info(x, y):
    print("Turtle Info")
    for i in range(len(all_turtles)):
        t = all_turtles[i]
        if t.distance(x, y) < 20:
            info = turtle_data[i]
            print(f'Turtle {i}: {info}')

screen.onclick(show_turtle_info)

def game_loop():
    move_turtles()
    screen.ontimer(game_loop, 2000)

game_loop()
screen.mainloop()


'''
1. Count Word Occurrences
Write a program that asks the user for a sentence and counts how many times each word appears.
and print the most frequent word

Input: "cat dog cat"
Output: {'cat': 2, 'dog': 1}
'''