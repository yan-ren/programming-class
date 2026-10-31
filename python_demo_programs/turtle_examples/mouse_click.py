import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Mouse Clicking Game")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

# Score variables
score = 0

# Turtle for displaying the score
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color("black")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 260)
score_turtle.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Function to update the score
def update_score():
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Create multiple targets
targets = []

def create_target():
    target = turtle.Turtle()
    target.shape("circle")
    target.color("red")
    target.penup()
    target.speed(0)
    targets.append(target)
    return target

# Function to move a target to a random spot on the screen
def move_target(target):
    target.goto(random.randint(-390, 390), random.randint(-290, 290))
    wn.ontimer(lambda: move_target(target), 3000)  # Move target every 3 seconds

# Function to handle the click event
def click_target(x, y, target):
    global score
    score += 1
    update_score()
    move_target(target)

# Bind the click event to each target
def bind_click_event(target):
    target.onclick(lambda x, y: click_target(x, y, target))

# Initialize targets and bind the click events
def setup_targets():
    for _ in range(5):
        target = create_target()
        move_target(target)
        bind_click_event(target)

# Main game loop
setup_targets()
wn.mainloop()
