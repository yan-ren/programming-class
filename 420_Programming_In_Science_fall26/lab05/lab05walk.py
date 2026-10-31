import random
import turtle

steps = int(input('How many steps should the turtle take? '))

walker = turtle.Turtle()
walker.speed(5)
step_size = 20

i = 0
while i < steps:
    direction = random.randint(1,4) # give random integer from 1 to 4 inclusive

    if direction == 1:
        # north
        walker.setheading(90)
    elif direction == 2:
        # west
        walker.setheading(180)
    elif direction == 3:
        # south
        walker.setheading(270)
    else:
        # east
        walker.setheading(0)

    walker.forward(step_size)
    i += 1

turtle.done()