# import time
#
#
# number = int(input('Enter a number:'))
# print('You just entered:', number)

# i = 0
# while i < number:
#     print('Hello')
#     i += 1

# count down from input number to 0
# while number >= 0:
#     print(number)
#     number -= 1
#     time.sleep(1)

# Write a while loop that prints all multiples of 3 less than 30.
# i = 1
# while i <= 30:
#     if i % 3 == 0:
#         print(i)
#     i += 1
import random

target = random.randint(0, 20)
chance = 3

while chance > 0:
    guess = int(input('Guess a number between 0 to 20'))

    if guess > target:
        print('Too high')
    elif guess < target:
        print('Too low')
    else:
        print('Correct')
        exit(0)

    chance -= 1

# follow up question: using input function to ask user to give a random range