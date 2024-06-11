import turtle
import random

# Setup the screen
wn = turtle.Screen()
wn.title("Turtle Dictionary Example")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turn off automatic screen updates

# Dictionary to store turtle properties
turtle_properties = {
    "turtle1": {"color": "red", "shape": "turtle", "speed": 1},
    "turtle2": {"color": "green", "shape": "turtle", "speed": 2},
    "turtle3": {"color": "blue", "shape": "turtle", "speed": 3},
    "turtle4": {"color": "yellow", "shape": "turtle", "speed": 4},
    "turtle5": {"color": "purple", "shape": "turtle", "speed": 5}
}

# Initialize turtles based on the dictionary
turtles = {}

for name, props in turtle_properties.items():
    t = turtle.Turtle()
    t.color(props["color"])
    t.shape(props["shape"])
    t.penup()
    t.speed(0)  # Set animation speed to the max for smooth movement
    t.goto(random.randint(-380, 380), random.randint(-280, 280))
    turtles[name] = t


# Function to move turtles around the screen
def move_turtles():
    for name, t in turtles.items():
        t.forward(turtle_properties[name]["speed"])
        # Bounce back if the turtle hits the screen edge
        if t.xcor() > 390 or t.xcor() < -390:
            t.right(180)
        if t.ycor() > 290 or t.ycor() < -290:
            t.right(180)

    wn.update()  # Update the screen
    wn.ontimer(move_turtles, 20)  # Schedule the next move


# Start moving the turtles
move_turtles()

# Keep the window open
wn.mainloop()
