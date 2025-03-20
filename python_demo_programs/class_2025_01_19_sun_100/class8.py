# '''
# Convert this guessing game into a turtle based graphic game
# '''
# import random
# import turtle
#
# screen = turtle.Screen()
# screen.setup(800, 600)
#
# pen = turtle.Turtle()
# pen.hideturtle()
# pen.speed(0)
# pen.penup()
# pen.goto(0, 200)
#
# pen.write('Welcome to the number guessing game',
#           align='center', font=('Arial', 24, 'normal'))
#
# chance = 3
# target = random.randint(1, 10)
# while chance > 0:
#     guess = int(screen.textinput('Guess a number', 'Guess a number'))
#     pen.clear()
#     if guess == target:
#         pen.color('green')
#         pen.write('Guess Correct!',
#                   align='center', font=('Arial', 24, 'normal'))
#         pen.goto(100, 100)
#
#         break # break exists from the loop immediately
#     elif guess > target:
#         pen.color('red')
#         pen.write('Guess too high!',
#                   align='center', font=('Arial', 24, 'normal'))
#     elif guess < target:
#         pen.color('red')
#         pen.write('Guess too low!',
#                   align='center', font=('Arial', 24, 'normal'))
#     chance -= 1
#
# turtle.done()
#
#

# calculate the sum of all number from 1 to 100
# use while loop
# number = 1
# s = 0
# while number <= 100:
#     s = s + number
#     number += 1
#
# print(s)
#
# # calculate the sum of all even number under 100
# number = 1
# s = 0
# while number <= 100:
#     if number % 2 == 0:
#         s = s + number
#     number += 1
#
# print(s)

import turtle

screen = turtle.Screen()
screen.setup(800, 600)

pen = turtle.Turtle()

j = 0
while j < 10:
    i = 0
    while i < 4:
        pen.forward(100)
        pen.left(90)
        i += 1
    pen.left(10)
    j += 1

turtle.done()