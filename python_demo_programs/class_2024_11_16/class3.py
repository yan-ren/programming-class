'''
control flow:
1. conditional: if elif else
2. looping: repeat
'''
# import time
#
#
# i = 10
# while i > 0:
#     print(i)
#     i -= 1
#     time.sleep(1)

# print all even number under 20
# i = 0
# while i < 20:
#     print(i)
#     i += 2
#
# i = 0
# while i < 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# s = 'ello'
# index = 0
#
# while index < len(s):
#     print(s[index])
#     index += 1

# check palindrome using loop
# s = 'boob'
# index = 0
# is_palindrome = True
# while index < len(s) / 2:
#     if s[index] != s[len(s) - index - 1]:
#         is_palindrome = False
#     index += 1
#
# if is_palindrome:
#     print('Is palindrome')
# else:
#     print('Not palindrome')

'''
guessing a number

define a target number 
ask user for a number, if the number is equal to the target, stop asking, finish the program
if guess is higher than target, print 'too high' and ask user to guess again
if guess is lower, print 'too low' and ask user to guess again
'''
import random


running = True
target = random.randint(0, 20)
chance = 3

while running:
    number = int(input('Enter a number between 0 to 20:'))

    if number > target:
        print('too high')
    elif number < target:
        print('too low')
    else:
        print('correct')
        running = False

    chance -= 1

    if chance == 0:
        running = False
        print('Game Over')

'''
exercise:

Average calculator, e.g. 
user keeps entering numbers until enter a finish word, such as “end”. 
Calculate the average basing on all user inputs
'''
'''
Two keywords used inside the loop
- break: stop the loop immediately
- continue: stop the current loop start next one
'''

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

'''
prime number

'''

number = 80
i = 2
is_prime = True
while i < number:
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print('prime')
else:
    print('not prime')

