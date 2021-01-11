import random
# import time
# # module
# n = int(input('enter a number:'))
#
# while n > 0:
#     print(n)
#     time.sleep(1)
#     n -= 1

# print all even numbers under 100
# n = 2
# while n < 100:
#     print(n)
#     n += 2
#
# # method 2
# n = 1
# while n < 100:
#     if n % 2 == 0:
#         print(n)
#     n += 1

# guessing number
# target = random.randint(0, 100)
# done = False
#
# while not done:
#     guess = int(input('guess a number between 0 to 100:'))
#     if guess == target:
#         print('correct')
#         done = True
#     elif guess > target:
#         print('guessing too high')
#     elif guess < target:
#         print('guessing too low')

# average calculator
# done = False
# sum = 0
# counter = 0
#
# while not done:
#     number = input('enter the number:')
#     if number == 'end':
#         done = True
#     else:
#         number = int(number)
#         sum += number
#         counter += 1
#
# print('average is', sum/counter)

counter = 5
# counter = 5, 4, 3, 2, 1
# counter2 = counter
# 5, 4, 3, 2, 1
# 4, 3, 2, 1
# 3, 2, 1
# 2, 1
# 1
# while counter > 0:
#     counter2 = counter
#     while counter2 > 0:
#         print(counter2)
#         counter2 -= 1
#     counter -= 1

# palindrome
# method 1, revered string
# text = input('enter a word:')
# text_reverse = text[::-1]
# if text == text_reverse:
#     print('palindrome')
# else:
#     print('not palindrome')

# method 2, while loop
#  k a y a k
'''
counter = 1
len(text)-1-counter = 5-1-1 = 3
text[counter] == text[0] == 'k'
text[len(text)-1-counter] == text[4] == 'k'
'''
text = input('enter a word:')

counter = 0
palindrome = True
while counter < len(text) / 2:
    if text[counter] != text[len(text) - 1 - counter]:
        palindrome = False
    counter += 1

if palindrome:
    print('palindrome')
else:
    print('not palindrome')
