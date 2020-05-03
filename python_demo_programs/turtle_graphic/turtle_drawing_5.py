import turtle

wn = turtle.Screen()
tess = turtle.Turtle()
tess.speed(10)

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for i in range(360):
    tess.pencolor(colors[i % 6])
    tess.width(i / 100 + 1)
    tess.forward(i)
    tess.left(59)

wn.exitonclick()