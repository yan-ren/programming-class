'''
Given a list of numbers find how many positive and how many negative

'''

# numbers = [1, 2, -1, 3, 2, -4]
# negative = 0
# positive = 0
#
# for num in numbers:
#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
#
# print(positive)
# print(negative)
#
# negative = 0
# positive = 0
#
# i = 0
# while i < len(numbers):
#     if numbers[i] > 0:
#         positive += 1
#     elif numbers[i] < 0:
#         negative += 1
#     i += 1
# print(positive)
# print(negative)

import random


word_list = ['apple', 'banana', 'grape', 'cherry', 'orange']
secret_word = random.choice(word_list)
guessed_letters = []
display_word = []
for _ in secret_word:
    display_word.append('_')

tries = 6

print("Welcome to the Word Guessing Game!")
print("Try to guess the word, one letter at a time.")

while tries > 0 and '_' in display_word:
    print('Word:', ' '.join(display_word))
    print('Guessed letters:', guessed_letters)

    guess = input('Guess a letter: ').lower()
    if guess in guessed_letters:
        print('You already guessed that letter')
        tries -= 1
        continue
    guessed_letters.append(guess)

    if guess in secret_word:
        print('Good guess')
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print('Wrong guess')
        tries -= 1
        print('Tries left:', tries)