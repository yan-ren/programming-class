import turtle

wn = turtle.Screen()
wn.setup(800, 600)

t = turtle.Turtle()
t.shape('turtle')
t.speed(3)
turtle.colormode(255)
t.fillcolor((173, 255, 74))

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

wn.exitonclick()
