import turtle

wn = turtle.Screen()
wn.screensize(800, 600)
alex = turtle.Turtle()
alex.pensize(3)

colors = ['coral', 'cyan', 'gold', 'lavender', 'LightGrey']
shape_numbers = 24

for k in range(shape_numbers):
    for i in colors:
        alex.color(i)
        alex.forward(100)
        alex.left(72)
    alex.left(360 / shape_numbers)

wn.exitonclick()