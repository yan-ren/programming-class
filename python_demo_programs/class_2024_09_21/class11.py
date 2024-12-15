# names = ['Tom', 'Jerry']
# for n in names:
#     n = "MR." + n
#
# print(names)
#
# i = 0
# while i < len(names):
#     names[i] = 'MR.' + names[i]
#
# print(names)

'''
Given a list of number and a target number, find how many target number exists in the list
example:
number = [1, 2, 1, 2, 4, 1]
target = 1

output = 3
'''

numbers = [1, 2, 1, 2, 4, 1]
target = 1
# count = 0
#
# for v in numbers:
#     if v == target:
#         count += 1
#
# print(count)

# print(numbers.count(target))
# print(max(numbers))
# print(min(numbers))
# # find the index of first occurrence of a given number
# print(numbers.index(4))
# numbers.sort()
# print(numbers)

'''
|2| = 2
|-2| = 2

given a list of numbers, if number is positive, leave as it, if number is negative,
change it to positive
'''
# numbers = [1, -1, 2, -3]
# i = 0
# while i < len(numbers):
#     if numbers[i] < 0:
#         numbers[i] = numbers[i] * -1
#
#     i += 1
import random


# words = ['python', 'list', 'coding', 'program', 'developer']
#
# # randomly choose a word
# word = random.choice(words)
#
# print(word)
# w = list(word)
# print(w)
# random.shuffle(w)
# print(w)
# # put list back to a string
# scrambled_word = ''.join(w)
# print(scrambled_word)

# items = ["🍎", "🍌", "🍇", "🍓", "🍉", "🍒"]
# # print(items)
# pairs = items * 2
# print(pairs)

import time

emojis = ["🍎", "🍌", "🍇", "🍓", "🍉", "🍒", "🍍", "🥝", "🥭", "🍑"]
original_list = random.sample(emojis, 5)
print(original_list)

time.sleep(3)
print("\n" * 100) # clear the console
# generate 3 incorrect options and shuffle
options = [original_list]
while len(options) < 4:
    shuffled = random.sample(emojis, 5)
    if shuffled not in options:
        options.append(shuffled)

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


'''
if you are given two list, how to know they are the same

[1, 2]
[2, 1]
they are not the same

exercise: write a program to check if two lists are same
'''
a = [1, 2, 3]
b = [1, 2, 3]

still_true = True

if len(a) != len(b):
    still_true = False
else:

    for i in range(len(a)):
        if a[i] != b[i]:
            still_true = False
            break

print(still_true)
