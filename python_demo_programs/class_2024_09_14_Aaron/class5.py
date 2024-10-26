'''
control flow
- conditional: if else
- loop:
'''
# i = 0
# while i <= 10:
#     print(i)
#     i = i + 1 # i += 1
#
# print(i)
# import time
#
# counter = int(input('Enter a number for counting dow:'))
#
# while counter > 0:
#     print(counter)
#     counter -= 1
#     time.sleep(1)

# find all even numbers under 20
# import random
#
# target = random.randint(0, 20)
#
# print('Guess a number between 0 to 20')
# guess = int(input('Guess:'))
#
# while guess != target:
#     if guess > target:
#         print('Too high')
#     else:
#         print('Too low')
#     guess = int(input('Guess:'))
#
# print('Guess correctly')

# exercise: add program that can finish the game if user guesses over 3 times without correct anwser

import turtle

window = turtle.Screen()
window.setup(600, 800)

t = turtle.Turtle()

i = 0
while i < 3:
    t.forward(100)
    t.left(120)
    i += 1

turtle.done()