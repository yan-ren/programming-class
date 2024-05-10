import turtle


wn = turtle.Screen()
t = turtle.Turtle()
# t.forward(50)
# t.left(90)
# t.forward(50)
color = input('which color do you want to use: ')
t.fillcolor(color)

t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(50, 50)
t.pendown()

t.begin_fill()
t.circle(20)
t.end_fill()

turtle.done()
