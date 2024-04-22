import turtle

window = turtle.Screen()
window.setup(800, 800)

tina = turtle.Turtle()
tina.fillcolor("black")

# first circle
tina.begin_fill()
tina.circle(100)
tina.end_fill()

# second circle
tina.penup()
tina.goto(75, 175)
tina.pendown()
tina.begin_fill()
tina.circle(50)
tina.end_fill()


turtle.done()
