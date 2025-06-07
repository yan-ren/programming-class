# x = 2
#
# def foo(y):
#     x = 41
#     z = 5
#     print(locals())
#     print(globals()['x'])
#     print(x, y, z)
#
# foo(3)

import random

words = ['python', 'variable', 'loop', 'index']
chosen_word = random.choice(words)

attempts = 3
word_length = len(chosen_word)
display_word = ['_'] * word_length

print('Welcome to Word Slicer!')
print(f'The word has {word_length} letters')

while attempts > 0:
    reveal_index = random.randint(0, word_length - 1)
    display_word[reveal_index] = chosen_word[reveal_index]
    print("\nCurrent word: " + " ".join(display_word))
    print(f"Attempts left: {attempts}")

    guess = input('Guess the word:')
    if guess == chosen_word:
        print(f"Congratulations! You've guessed the word: {chosen_word}")
        break

    attempts -= 1
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was: {chosen_word}")