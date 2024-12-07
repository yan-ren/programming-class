'''
review:
while loop
for loop

list
'''
# names = ['Tom', 'Jerry', 'Tim']
# print(names)
# print(names[0])
# print(names[1])
#
# # how to print each value using loop(while/for)
# # while
# index = 0
# while index < len(names):
#     print(names[index])
#     index += 1
#
# # for
# for name in names:
#     print(name)
#
#
# numbers = []
# numbers.append(1)
# numbers.append(2)
# print(numbers)
#
# # delete by index
# del numbers[0]

# given a list of numbers, calculate the sum, using loop
numbers = [3, 1, 2, 12, 5]
# sum = 0
# for n in numbers:
#     sum += n
#
# print(sum)
# print(sum(numbers))

#
# given a list of numbers, find the maximum, assume each number of show once
# numbers = [-1, -2, -20, -12, -3]
# max_number = numbers[0]
#
# for n in numbers:
#     if n > max_number:
#         max_number = n
#
# print(max_number)

import random

numbers = [1, 2, 3, 4, 5, 6]

for i in range(10):
    print(random.choice(numbers))

'''
homework

Given a list of numbers, 
create a new list only with the positive numbers from the original list
hint: use loop and append

given: [1, 2, -1, 4, -3]
new: [1, 2, 4]
'''