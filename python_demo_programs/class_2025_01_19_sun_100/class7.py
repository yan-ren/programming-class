'''
Today: Looping - repeat
- while loop
- for loop

Conditional
if elif else
- makes program more flexible by giving option
'''

# day = input('What day is it today?')
# if day == 'monday':
#     print('School day')
# elif day == 'tuesday':
#     print('School day')

# print hello 10 times
# i = 0
# while i < 10: # i = 10
#     print('hello')
#     i = i + 1
#
# print(i)
#
# # how to print from 1 to 10 using while loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1 # i = i + 1

# how to print from 10 to 1 using while loop
# import time
#
# i = int(input('Enter a number for counting down:'))
# while i > 0:
#     print(i)
#     i -= 1
#     time.sleep(1)

# exercise1: math problem, how to print all even number under 20
# solution1
# number = 2
# while number <= 20:
#     print(number)
#     number += 2
#
# # solution2
# number = 1
# while number <= 20:
#     if number % 2 == 0: # remember % calculates the remainder of division
#         print(number)
#     number += 1
import time
import random

# while True:
#     number = random.randint(1, 6)
#     print(number)
#     time.sleep(3)

running = True
target = random.randint(1, 10)
while running:
    guess = int(input('Guess a number:'))
    if guess == target:
        print('Guess correct!')
        running = False
    elif guess > target:
        print('Guess too high!')
    elif guess < target:
        print('Guess too low')

# follow up:
# how to give more details about guess, e.g. guess too high? guess too low?