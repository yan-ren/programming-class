# draw color-filled square in turtle
import turtle

# creating turtle pen
t = turtle.Turtle()

col = 'red'

# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the square of side s
for _ in range(4):
    t.forward(100)
    t.right(90)

t.circle(40)
# ending the filling of the color
t.end_fill()

turtle.done()
