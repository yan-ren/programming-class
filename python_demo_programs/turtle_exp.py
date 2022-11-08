import turtle

# creates a graphics window
wn = turtle.Screen()
# create a object called alex
alex = turtle.Turtle()
# for i in range(4):
#     alex.forward(150)
#     alex.left(90)
turtle.bgcolor("blue")
alex.pencolor("green")
for i in range(50):
    alex.forward(10*i)
    alex.right(144)

wn.exitonclick()
