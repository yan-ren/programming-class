'''
exercise 1:
using loop to calculate the sum from 1 to 100, e.g. 1+2+3+...+99+100

exercise 2:
using loop to show all even numbers under 100
'''
import sys
# sum = 0
# index = 1
# while index <= 100:
#     sum += index    # sum = sum + i
#     index += 1      # i = i + 1
#
# print(sum)

# index = 0
# while index <= 100:
#     print(index)
#     index += 2

# index = 0
# while index <= 100:
#     if index % 2 == 0:
#         print(index)
#     index += 1

import turtle
import time
import random

wn = turtle.Screen()
wn.setup(800, 800)

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.penup()

# turtle object to draw the food
food = turtle.Turtle()
food.shape('circle')
food.color('green')
food.penup()
food.speed(0)
food.goto(random.randint(-390, 390), random.randint(-390, 390))

# add keyboard control
turtle.onkeypress(lambda: snake.setheading(90), "Up")
turtle.onkeypress(lambda: snake.setheading(-90), "Down")
turtle.onkeypress(lambda: snake.setheading(180), "Left")
turtle.onkeypress(lambda: snake.setheading(0), "Right")
turtle.listen()

while True:
    snake.forward(3)
    snake.stamp()
    snake.clearstamps(1)

    if snake.distance(food) < 20:
        food.goto(random.randint(-390, 390), random.randint(-390, 390))
        snake.stamp()
        snake.stamp()

    # check if snake x coordinate is within the screen
    if snake.xcor() > 400 or snake.xcor() < -400:
        sys.exit(0)

    # check if snake y coordinate is within the screen
    if snake.ycor() > 400 or snake.ycor() < -400:
        sys.exit(0)

    time.sleep(0.01)


'''
exercise:
1. write a program print all number which are divisible by 7 and divisible by 5, between 100 to 200 (both included)

2. 
Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number 
and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
Sample Output :
1
2
fizz
4
buzz
...
'''

# q1
number = 100
while number <= 200:
    if number % 7 == 0 and number % 5 == 0:
        print(number)

    number += 1

# q2
number = 1
while number <= 50:
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)

    number += 1
