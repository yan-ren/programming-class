# s = 'Arthur'
#
# print(s[3])
# print(len(s))
# # print(s[0:2])
# new_s = s[0:2]
# print(new_s)

# palindrome: write a program to determine if a word is palindrome or not
# string + if else
# word = input('enter a word:')
# if word == word[::-1]:
#     print('The word is palindrome')
# else:
#     print('The word is not palindrome')

# print(not (1 == 1 and 0 != 1))

# counter = 1
# while counter <= 10:
#     print(counter)
#     counter = counter + 1

# import time
#
#
# counter = int(input('enter a number to start counting down:'))
# while counter >= 1:
#     print(counter)
#     counter = counter - 1
#     time.sleep(1)

# number = 2
# while number <= 100:
#     print(number)
#     number += 2

# number = 1
# while number <= 100:
#     if number % 2 == 0:
#         print(number)
#     number += 1

import random


target = random.randint(1, 20)
run = True

while run:
    guess = int(input('Guess a number between 1 to 20:'))
    if guess == target:
        print('correct')
        run = False
    elif guess > target:
        print('your guess is bigger than correct answer')
    else:
        print('your guess is smaller than correct answer')