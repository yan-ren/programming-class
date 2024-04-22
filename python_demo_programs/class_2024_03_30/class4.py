# import random
#
# # target = random.randint(1, 100)
# target = 2
# chance = 5
# correct = False
#
# while correct == False and chance > 0:
#     chance = chance - 1
#     guess = int(input('Guess a number: '))
#     if guess == target:
#         # print('Correct!')
#         correct = True
#     elif guess > target:
#         print('Too high, guess again')
#     else:
#         print('Too low, guess again')
#
# if correct:
#     print('You win')
# else:
#     print('You lose')

# palindrome: bob, kayak,

# number = 122221
# word = str(number)
# word_length = len(word)
#
# index = 0
# is_palindrome = True
# while index < word_length / 2:
#     if word[index] != word[word_length - 1 - index]:
#         is_palindrome = False
#     index = index + 1
#
# if is_palindrome:
#     print('word is palindrome')
# else:
#     print('word is not palindrome')

# print(len(str(5 / 2)))
# print(5 // 2)

'''
Given a number, print all prime number under the given number
'''
# step 1: check if a single number is a prime

# limit = 20
# while limit > 1:
#     factor = 2
#     is_prime = True
#     while factor < limit:
#         if limit % factor == 0:
#             is_prime = False
#         factor += 1
#
#     if is_prime:
#         print(str(limit) + ' prime number')
#
#     limit -= 1

# step 2: print all prime number under a limit

# dynamic type
numbers = ['a', 'b', 1, 2, 3, 4, 5]
numbers.append(6)

print(numbers)

