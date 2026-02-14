import turtle

screen = turtle.Screen()
screen.setup(800, 800)

pen = turtle.Turtle()
pen.color('green')

pen.begin_fill()
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(120)
pen.end_fill()

pen.color('orange red')
pen.penup()
pen.goto(-100, -100)
pen.pendown()

pen.begin_fill()
pen.circle(50)
pen.end_fill()

turtle.done()
