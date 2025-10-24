import turtle
import random
import time

turtle.setup(600, 400)
turtle.bgcolor("lightblue")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 100)
pen.write("Welcome to Guess the Number!", align="center", font=("Arial", 18, "bold"))

secret = random.randint(1, 20)

for attempt in range(1, 4):
    guess = turtle.numinput('Your guess', f'Attempt {attempt}: enter a number 1-20')

    pen.goto(0, 0)
    pen.clear()

    if guess == secret:
        pen.write(f"Correct! The number was {secret}!", align="center", font=("Arial", 16, "bold"))
        break
    elif guess < secret:
        pen.write("Too low! Try again.", align="center", font=("Arial", 14, "normal"))
    else:
        pen.write("Too high! Try again.", align="center", font=("Arial", 14, "normal"))

    if attempt == 3 and guess != secret:
        pen.goto(0, -50)
        pen.write(f"Out of tries! The number was {secret}.", align="center", font=("Arial", 14, "normal"))

    time.sleep(1)

turtle.done()
