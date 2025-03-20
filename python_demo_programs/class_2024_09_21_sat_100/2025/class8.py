# def print_message():
#     print('Welcome to the class')
#     print('Today is a good day')
#
# print_message()
# print_message()

# create a function with input
# def welcome(name):
#     print('Welcome', name)
#     print('Today is warm day')
#
#
# welcome('Tom')

import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor('white')

counter = turtle.Turtle()
counter.hideturtle()
counter.penup()

def count_down():
    screen.tracer(0) # turn off the screen auto update
    timer = 10
    colors = ['lightblue', 'lightgreen', 'yellow', 'pink']
    # write a count down from timer to zero
    while timer >= 0:
        screen.clear()
        screen.bgcolor(random.choice(colors))
        counter.write(timer, align="center", font=("Arial", 48, "bold"))
        screen.update()
        timer -= 1
        time.sleep(1)

def finish():
    screen.clear()
    for _ in range(6):
        screen.bgcolor(random.choice(["red", "orange", "purple", "blue"]))
        counter.write("Time's up!", align="center", font=("Arial", 48, "bold"))
        screen.update()
        time.sleep(0.5)
        screen.clear()
        time.sleep(0.5)


count_down()
finish()
turtle.done()

# write a function which takes a list of numbers, then calculate the sum
def sum(numbers):
    s = 0
    for num in numbers:
        s += num

    # print(s)
    return s

print(sum([1, 2, 3]))

# exercise: write a function which takes a list of numbers,
# count how many positive number in the list
def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1

    return count

print(count_positive([1, 2, -1, -2, 1]))
