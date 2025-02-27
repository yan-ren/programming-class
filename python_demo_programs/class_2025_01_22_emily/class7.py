
# while True:
#     print('hello')
#
# print('finish')

# name1 = 'Tom'
# name2 = 'Jerry'
# name3 = 'Peggy'

'''
list is a basic data structure
'''
import os

names = ['Tom', 'Jerry', 'Peggy'] # mutable
print(names[0])
print(names[1:])
names[1] = 'Jay'
print(names)

# text = 'abcde' # immutable
# print(text[2])
# print(text[2:])
# text[2] = 'w'

# add value at position
names.insert(0, 'Zoe')
print(names)

# add value in the end
names.append('Kim')
names.append('Kim')
print(names)

# remove value from the list
names.remove('Kim')
print(names)

del names[0]
print(names)

if 'no name' in names:
    names.remove('no name')

# del names[100]
# value = names.pop(0) # remove the first value
# print(value)
#
# print(names.count('Kim')) # return the number of 'Kim
# names.index('Kim')

# name = ['Tom Jerry Peggy Kim Kim', 'Kim']
# print(name.count('Kim'))

numbers = [1, 10, 2, 4, 5] # [2, 11, 3, 5, 6]

# use loop with list
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1
#
#
# for index in range(len(numbers)):
#     print(numbers[index])
#
#
# for num in numbers:
#     print(num)

numbers = [1, 10, 2, 4, 5]

# increment each value in numbers by one
# [2, 11, 3, 5, 6]

# not working
# for num in numbers: # for each loop
#     num += 1
#     print(num)
#
# print(numbers)
#
# working
# for index in range(len(numbers)):
#     numbers[index] += 1
#     print(numbers[index])
# print(numbers)
#
# index = 0
# while index < len(numbers):
#     numbers[index] += 1
#     index += 1

numbers = [-2, -11, -11, -5, -6]
# find the largest value from the list
# option 1: sorting
# numbers.sort()
# numbers[-1]

# option 2: max
# print(max(numbers))

# option 3: loop + if
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

print(max_num)
