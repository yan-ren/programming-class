'''
function/method
'''
import random
import time
# numbers = [1, 2, 3, 1, 4]
# sum = 0
# for value in numbers:
#     sum += value
#
# numbers = [1, 2, 3]

# def welcome(name):
#     print('welcome to the class', name)
#     print('today is a good day')
#
#
# welcome('Tom') # call the function by giving input
# welcome('Jerry')
#
# def list_sum(l):
#     sum = 0
#     for value in l:
#         sum += value
#
#     print(sum)
#
# list_sum([1, 2, 3])
# list_sum([2, 3, 4, 5])

# exercise: write a function which takes a list of numbers as input,
# then calculate the average

import turtle
import time

window = turtle.Screen()
window.setup(800, 800)

# create a snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.penup()

# create food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('green')
food.penup()
food.goto(random.randint(-200, 200), random.randint(-200, 200))

def move_up():
    snake.setheading(90)

def move_down():
    snake.setheading(-90)

def move_left():
    snake.setheading(180)

def move_right():
    snake.setheading(0)

turtle.listen()
turtle.onkeypress(move_up, 'Up')
turtle.onkeypress(move_down, 'Down')
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')

score = 0

while True:
    snake.forward(5)
    # leave a new mark
    snake.stamp()
    # clear the oldest mark
    snake.clearstamps(1)

    time.sleep(0.01)

    if snake.xcor() > 400 or snake.xcor() < -400:
        break

    if snake.ycor() > 400 or snake.ycor() < -400:
        break

    if snake.distance(food) < 20:
        food.goto(random.randint(-200, 200), random.randint(-200, 200))
        snake.stamp()
        score += 1
        print('Score:', score)

turtle.done()
