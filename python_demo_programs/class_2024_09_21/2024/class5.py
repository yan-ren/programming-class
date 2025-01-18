'''
control flow
- conditional: if elif else
- loop: while, for
'''
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1 # i += 1

# exercise: count down from 10 to 1
# import time
#
#
# i = int(input('Enter the number for counting down:'))
# while i >= 1:
#     print(i)
#     i = i - 1 # i -= 1
#     time.sleep(1)

# how to print all even numbers under 20
# method 1
# i = 2
# while i < 20:
#     print(i)
#     i += 2
#
# # method 2
# i = 1
# while i < 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# import turtle
#
#
# screen = turtle.Screen()
# screen.setup(600, 800)
#
# pen = turtle.Turtle()
#
# j = 0
# while j < 4:
#     i = 0
#     while i < 4:
#         pen.forward(100)
#         pen.left(90)
#         i += 1
#     pen.left(15)
#     j += 1
#
# turtle.done()


import random


target = 12
chance = 3
running = True

while running:
    guess = int(input('Guess a number between 0 to 20'))
    chance -= 1
    if guess > target:
        print('Too high')
    elif guess < target:
        print('Too low')
    else:
        print('Correct')
        running = False

    if chance == 0:
        print('Game Over')
        running = False

# homework: only allow people to take 3 guess at maximum