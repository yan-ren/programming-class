# numbers = [1, 2]
# numbers.append(10)
# print(numbers)
#
# numbers = []
# numbers.pop(0)
# print(numbers)
#
# s = ['abc', 'hello']
# print(len(s))

numbers = [1, 2, 1, 4]

# how to use for loop to print each value
# for num in numbers:
#     num = num + 1

# how to use while loop to increment each value by one
index = 0
while index < len(numbers):
    numbers[index] += 1
    index += 1

print(numbers)

# find largest value from the list
print(max(numbers))
# find smallest value from the list
print(min(numbers))
# sort the list from smallest to the largest
numbers.sort(reverse=True)
print(numbers)

import random
import time
import turtle
# numbers = [1, 2, 3, 4, 5, 6]
#
# for i in range(10):
#     print(random.choice(numbers))
#     time.sleep(1)

screen = turtle.Screen()
screen.setup(600, 600)

pen = turtle.Turtle()

d1 = [1, 2, 3, 4, 5, 6]
d2 = [1, 2, 3, 4, 5, 6]

v1 = random.choice(d1)
v2 = random.choice(d2)

