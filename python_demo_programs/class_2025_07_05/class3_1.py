'''
data structure

1. tuple
2. list
3. dictionary
4. set

'''

# names = ['Terry', 'Tod', 'Kitty']
#
# print(names[0])
# names[0] = 'Tom'
#
# names.append('Ted')
# names.insert(1, 'Tim')
# print(names)
#
# names.remove('Tom')
# del names[0]


numbers = [1, 2, 2, 2, 3, 4, 1]

# i = 0
# while i < len(numbers):
#     if numbers[i] == 2:
#         del numbers[i]
#     else:
#         i += 1

# while 2 in numbers:
#     numbers.remove(2)

# for num in numbers:
#     print(num)

# for num in numbers:
#     num += 1
#
# print(numbers)

# numbers = [1, -2, 3, -4, 2, 1]
# create a new_numbers list only keeps the positive

# numbers = [[1, 2, 3], [2, 3, 4]]

# import random
# import time
#
#
# emojis = ["🍎", "🍌", "🍇", "🍓", "🍉", "🍒", "🍍", "🥝", "🥭", "🍑"]
# original = random.sample(emojis, 5)
# print(original)
#
# time.sleep(3)
# print('\n' * 100)
# options = [original]
# while len(options) < 4:
#     shuffled = random.sample(emojis, 5)
#     if shuffled not in options:
#         options.append(shuffled)
#
# random.shuffle(options)
# print('Which one is correct?')
# id = 0
# for option in options:
#     print(id, option)
#     id += 1
#
# choice = int(input('Enter the number for the correct option: '))
# if options[choice] == original:
#     print('Correct')
# else:
#     print('Wrong')

# numbers = (1, 2, 1, 4)
# print(type(numbers))
# print(numbers[0])
# numbers[0] = 10

# s = 'abcdef'
# l = list(s)
# print(l)

# s = 'apple banana cherry'
# l = s.split(' ')
# print(l)

# s = '1 2 20 13 24'
# s = 'apple,banana,cherry'
# s.split(',')

# l = ['apple', 'banana', 'cherry']
# s = ','.join(l)
# print(s)

s = 'cG23mH-9s'
i = 0
uppercase = []
number = 0
while i < len(s):
    if 'A' <= s[i] <= 'Z':
        uppercase.append(s[i])
        i += 1
    elif s[i].isdigit() or s[i] == '-':
        start = i
        i += 1
        while i < len(s) and s[i].isdigit():
            i += 1
        number += int(s[start:i])
    else:
        i += 1

print(uppercase)
print(number)
result = ''.join(uppercase) + str(number)
print(result)