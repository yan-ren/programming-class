# '''
# use turtle, create a count down program
# '''
import turtle
import time
import random

def countdown(timer):
    screen.clear()
    screen.tracer(0)

    # if timer is 10
    while timer >= 0:
        # show this timer value on screen
        screen.clear()
        screen.bgcolor(random.choice(["white", "lightblue", "lightgreen", "yellow", "pink"]))

        font_size = 48 + (timer % 2) * 10  # Alternates between 48 and 58
        counter.write(timer, align="center", font=("Arial", font_size, "bold"))

        screen.update()
        timer -= 1
        time.sleep(1)

    screen.clear()

def finish():
    screen.clear()
    # Flashing final message effect
    for _ in range(6):
        screen.bgcolor(random.choice(["red", "orange", "purple", "blue"]))
        counter.write("Time's up!", align="center", font=("Arial", 48, "bold"))
        screen.update()
        time.sleep(0.5)
        screen.clear()
        time.sleep(0.5)

    counter.write("Time's up!", align="center", font=("Arial", 48, "bold"))
    screen.update()


screen = turtle.Screen()
screen.bgcolor('white')

# Setup turtle
counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(0, 0)

countdown(10)
finish()

turtle.done()

# def count(numbers):
#     # count function takes a list of number, return the number of positive values
#     count = 0
#     for value in numbers:
#         if value > 0:
#             count += 1
#
#     return count
#
# print(count([1, 2, -1, -2]))