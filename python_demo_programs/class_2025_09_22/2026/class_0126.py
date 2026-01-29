'''
homework:
use double loops, if statement, to make drawing of your choice
'''
# import turtle
#
# wn = turtle.Screen()
# wn.setup(800, 800)
#
# pen = turtle.Turtle()
# shape = wn.textinput('What do you want to draw', 'What do you want  to draw')
# if shape == 'square':
#     # possibly, can use double loop to make multiple squares
#     i = 0
#     while i < 4:
#         pen.forward(100)
#         pen.left(90)
#
# turtle.done()

'''
Today: Python list

list belongs to a data structure
'''
numbers = [1, 2, 1, 4, 2, 5]
# print(numbers)
#
# numbers.append(10)
# print(numbers)
# print(numbers[0])
# print(numbers[5])
# print(len(numbers))
# print(numbers[len(numbers) - 1])

# question: if you have a large list with many values
# how to access all values?

# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1

# if you have a list of numbers, how to calculate the sum of all numbers in the list
# e.g. [1, 2, 4, 1, 2]
# sum is 10

numbers = [1, 2, 4, 1, 2]
sum = 0
index = 0
while index < len(numbers):
    sum += numbers[index]
    index += 1
print(sum)

# if you have a list of numbers, how to find the largest numbers
# e.g. [1, 2, 4, 1, 2]
# largest value is 4
numbers = [-1, -2, -4, -1, -2]
largest = numbers[0] # assume first value is largest
# we cannot set the largest equals to zero, because zero may not be in the list

index = 0
while index < len(numbers):
    if numbers[index] > largest:
        largest = numbers[index]
    index += 1
print(largest)

# homework: find the smallest number from the list