# running = True
# sum = 0
# count = 0
# while running:
#     # ask user for input, if user type 'exit’ finish the loop
#     text = input('Enter a number or exit to stop the program')
#
#     if text == 'exit':
#         running = False
#     else:
#         sum += int(text)
#         count += 1
#
# print(sum/count)

# import random
#
#
# target = random.randint(0, 20)
# running = True
#
# while running:
#     guess = int(input('Guess a number between 0 to 20'))
#     if guess > target:
#         print('Too high')
#     elif guess < target:
#         print('Too low')
#     else:
#         print('Guess correct')
#         running = False

#
# number = 1
#
# while number <= 100:
#     i = 2
#     is_prime = True
#     while i < number:
#         if number % i == 0:
#             is_prime = False
#         i += 1
#     number += 1
#
#     if is_prime:
#         print(number)

'''
ask user entering number until user types 'exit'
when user types exit, print the largest number that user has typed in
'''
