import turtle


wn = turtle.Screen()
wn.setup(800, 600)

alex = turtle.Turtle()
alex.pensize(5)
alex.speed(8)

number_of_shapes = 72
for i in range(number_of_shapes):
    for color in ['yellow', 'red', 'purple']:
        alex.color(color)
        alex.forward(150)
        alex.left(120)

    alex.left(180 / number_of_shapes)


turtle.done()
