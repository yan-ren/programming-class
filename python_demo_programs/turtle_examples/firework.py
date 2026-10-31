import turtle
import random

# create a screen and setup the size
SCREEN_SIZE = 800
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)

# set up the background color for screen
wn.bgcolor("black")

# make a variable that we can control for drawing
my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.hideturtle()

# create a list to hold colors
colors = ['blue', 'red', 'yellow', 'orange', 'purple',
          'magenta', 'pink', 'lime',
          'green', 'gold', 'silver', 'violet']


# create a function that draws firework on the screen
def draw_firework(t):
    # make turtle go to the random place
    x = random.randint(-SCREEN_SIZE/2, SCREEN_SIZE/2)
    y = random.randint(-SCREEN_SIZE/2, SCREEN_SIZE/2)
    t.penup()
    t.goto(x, y)
    t.pendown()

    # select a color from the list
    t.color(random.choice(colors))

    # set a random size for firework
    size = random.randint(50, 150)

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
