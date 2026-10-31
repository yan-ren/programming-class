import turtle

wn = turtle.Screen()
tess = turtle.Turtle()
tess.speed(10)

for i in range(500):
    tess.forward(i)
    tess.left(89)

wn.exitonclick()