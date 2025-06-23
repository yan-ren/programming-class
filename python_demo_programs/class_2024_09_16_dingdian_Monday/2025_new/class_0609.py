import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Catch the Turtle!")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Score variable
score = 0

# Turtle for the game
catch_turtle = turtle.Turtle()
catch_turtle.shape("turtle")
catch_turtle.color("green")
catch_turtle.penup()
catch_turtle.speed(0)

# Turtle for displaying score
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 260)
score_turtle.write("Score: 0", align="center", font=("Arial", 18, "bold"))

# Function to move the turtle to a random location
def move_turtle():
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    catch_turtle.goto(x, y)
    screen.ontimer(move_turtle, 1000)  # Call again after 1 second

# Function to handle click
def turtle_clicked(x, y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))

# Start the game
catch_turtle.onclick(turtle_clicked)
move_turtle()

# Main loop
screen.mainloop()
