'''
string
'''
# s = 'abc'
# print(type(s))
#
# s = '123'
# print(type(s))
# s = 123
# print(type(s))
#
# s = ''
# s = ' '
#
# # length
# s = 'abc'
# print(len(s))
# s = ' '
# print(len(s))
#
# # create a program that asks user for a word and count how many letters in the word
# word = input('Enter a word:')
# print('There are', str(len(word)))

# s = 'abcdef'
# print(s[0])
# print(s[2])
# print(s[6])

# largest index = len - 1
# print(s[len(s) - 1])

# index = 0
# while index < 10:
#     print(index)
#     index = index + 1

import time

counter = int(input('Enter a number for counting down:'))

while counter > 0:
    print(counter)
    counter = counter - 1 # counter -= 1
    time.sleep(1)

