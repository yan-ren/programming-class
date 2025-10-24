# exercise: write a function that takes a list as input, return a new list with only even numbers
import random
import time


fruites = ['🍎', '🍉', '🍓', '🍒', '🍅', '🌶', '🍑', '🍠']

original_list = random.sample(fruites, 5)
print(original_list)

time.sleep(3)
print("\n" * 100)

options = [original_list]

while len(options) < 4:
    shuffle = random.sample(original_list, 5)
    if shuffle not in options:
        options.append(shuffle)

random.shuffle(options)
print('Which one is correct?')
id = 0
for option in options:
    print(id, option)
    id += 1

choice = int(input('Enter the number of the correct option: '))
if options[choice] == original_list:
    print('Correct!')
else:
    print('Wrong')