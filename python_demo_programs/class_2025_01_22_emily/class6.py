import turtle

screen = turtle.Screen()
screen.setup(800, 600)

t = turtle.Turtle()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# for i in range(4):
#     t.forward(100)
#     t.left(90)

# for i in range(3):
#     t.forward(100)
#     t.left(120)
#
# t.penup()
# t.goto(200, 200)
# t.pendown()

t.pencolor('dark orange')
t.fillcolor('dark orange')
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()


turtle.done()
