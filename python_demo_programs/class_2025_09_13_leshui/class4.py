# import random
# import time
#
# emojis = ["🍎", "🍌", "🍇", "🍓", "🍉", "🍒", "🍍", "🥝", "🥭", "🍑"]
# original = random.sample(emojis, 5)
#
# print(original)
# time.sleep(3)
# print('\n' * 100)
#
# options = [original]
# while len(options) < 4:
#     shuffled = random.sample(original, 5)
#     if shuffled not in options:
#         options.append(shuffled)
#
# random.shuffle(options)
# print('Which one is correct?')
#
# id = 0
# for option in options:
#     print(id, option)
#     id += 1
#
# choice = int(input('Enter the number of the correct:'))
# if options[choice] == original:
#     print('Correct')
# else:
#     print('Wrong')
#     choice = int(input('Enter the number of the correct:'))
#     if options[choice] == original:
#         print('Correct')
#     else:
#         print('Wrong')

# numbers = [1, 3, 2, 5, 'abc', [1, 2, 3]]

numbers = [[1, 3], [2, 4]]
print(len(numbers))
print(numbers[0][1])

# how to calculate the sum
s = 0
for sub in numbers:
    for value in sub:
        s += value

print(s)
