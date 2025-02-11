import turtle
import random

SCREEN_SIZE = 800
# create a screen and setup the size
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)

# set up the background color for screen
wn.bgcolor("black")

# make a variable that we can control for drawing
my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.hideturtle()
my_turtle.shape("square")

# create a list to hold colors
colors = ['blue', 'red', 'yellow', 'orange', 'purple',
          'magenta', 'pink', 'lime',
          'green', 'gold', 'silver', 'violet']


# create a function that draws firework on the screen
def draw_firework(t):
    # make turtle go to the random place
    x = random.randint(-SCREEN_SIZE/2, SCREEN_SIZE/2)
    y = random.randint(0, SCREEN_SIZE/2)
    y_cur = -SCREEN_SIZE/2
    t.penup()
    t.goto(x, y)
    t.pendown()

    # select a color from the list
    t.color(random.choice(colors))

    # set a random size for firework
    size = random.randint(50, 150)

    # going up
    start = turtle.Turtle()
    start.hideturtle()
    start.pencolor("White")
    start.pensize(3)
    start.speed(0)
    start.up()
    start.goto(x, y_cur)
    start.down()
    start.setheading(90)

    while y_cur < y:
        start.forward(10)
        start.up()
        start.forward(10)
        start.down()
        start.clear()
        y_cur = start.ycor()

    # draw firework
    for i in range(36):
        t.forward(size)
        t.backward(size)
        t.right(10)


for i in range(10):
    draw_firework(my_turtle)

my_turtle.penup()
my_turtle.goto(0, 300)
my_turtle.color("white")
my_turtle.write("Happy New Year!", align="center", font=("Verdana", 24, "normal"))

turtle.done()
