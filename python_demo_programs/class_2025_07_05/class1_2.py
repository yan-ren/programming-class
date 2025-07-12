# print(1+2)
# print(1-2)
# print('hello')
import turtle

window = turtle.Screen()

pen = turtle.Turtle()

# color = window.textinput('Choose a color', 'Choose a color')
color = 'red'
pen.color(color)

pen.penup()
pen.goto(100, 100)
pen.pendown()

pen.circle(40)

# pen.begin_fill()
# pen.forward(300)
# pen.left(90)
# pen.forward(300)
# pen.left(90)
# pen.forward(300)
# pen.left(90)
# pen.forward(300)
# pen.left(90)
# pen.end_fill()

turtle.done()