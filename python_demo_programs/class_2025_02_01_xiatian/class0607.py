# numbers = []
#
# numbers.append(2)
#
# numbers.extend([1, 2, 3, 4])

# how to create a list with number from 1...100
# [1, 2, 3, ..., 100]

# l1 = [1, 2]
# l2 = [3, 4]
#
# l1.append(l2)
# print(l1)
#
# l1.extend(l2)
# print(l1)
#
# del l1[0]
# print(l1)

'''
[
    [1, 2, 3],
    [2, 3]
]
'''
# numbers = [[1, 2], [2, 3]]
#
# s = 0
# for v in numbers:
#     for n in v:
#         s += n
#
# print(s)

import random
import time

emojis = ["🍎", "🍌", "🍇", "🍓", "🍉", "🍒", "🍍", "🥝", "🥭", "🍑"]
original_list = random.sample(emojis, 5)
print(original_list)

time.sleep(3)
print('\n' * 300)

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

choice = int(input('Enter the number of the correct option:'))
if options[choice] == original_list:
    print('Correct!')
else:
    print('Wrong!')


