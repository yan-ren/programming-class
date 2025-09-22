import turtle

wn = turtle.Screen()
wn.setup(800, 800)

t = turtle.Turtle()
t.speed(0)

'''
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
'''
t.color('red')
t.circle(60)

t.penup()
t.goto(100, 100)
t.pendown()
t.begin_fill()
t.circle(60)
t.end_fill()

turtle.done()
