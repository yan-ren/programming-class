'''

https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCJrProblemSet.html

Problem J1: Deliv-e-droid
'''
import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.setup(width=600, height=600)
screen.tracer(0)  # Disable automatic updates for faster drawing

grid = turtle.Turtle()
grid.hideturtle()
grid.speed(0)
grid.pensize(5)

def draw_grid():
    # draw 4 lines, two horizontal, two vertical
    grid.penup()
    grid.goto(-100, 300)
    grid.pendown()
    grid.goto(-100, -300)

    grid.penup()
    grid.goto(100, 300)
    grid.pendown()
    grid.goto(100, -300)

    grid.penup()
    grid.goto(-300, 100)
    grid.pendown()
    grid.goto(300, 100)

    grid.penup()
    grid.goto(-300, -100)
    grid.pendown()
    grid.goto(300, -100)


# draw X at position (x, y)
def draw_x(x, y):
    turtle.penup()
    turtle.goto(x - 60, y + 60)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.forward(120)
    turtle.penup()
    turtle.goto(x + 60, y + 60)
    turtle.pendown()
    turtle.setheading(-135)
    turtle.forward(120)


draw_grid()
screen.update()
turtle.done()