# write a program that print all the even number under 20
# number = 1
#
# while number <= 20:
#     if number % 2 == 0:
#         print(number)
#
#     number = number + 1

# given a list of numbers, find the largest number
# numbers = [-2, -1, -5, -3, -4]
#
# index = 0
# max_value = numbers[0]
# while index < len(numbers):
#     if numbers[index] > max_value:
#         max_value = numbers[index]
#
#     index = index + 1
#
# print(max_value)

# numbers = [1, 2, 3, 4]
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index = index + 1

# max_value = numbers[0]
# for v in numbers:
#     if v > max_value:
#         max_value = v

# exercise: given a list of numbers, find the sum of all numbers

# import turtle
# import random
#
#
# wn = turtle.Screen()
# wn.setup(800, 600)
# alex = turtle.Turtle()
#
# number_of_triangle = 72
# colors = ['yellow', 'red', 'purple']
#
# for i in range(number_of_triangle):
#     for i in range(3):
#         color = random.choice(colors)
#         alex.color(color)
#         alex.forward(150)
#         alex.left(120)
#     alex.left(360 / number_of_triangle)
#
# wn.exitonclick()

# for i in range(10):
#     print(i)
#
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

numbers = []
run = True

while run:
    number = int(input('enter a number:'))
    if number == -1:
        run = False
    else:
        numbers.append(number)

# calculate the average in number list
sum = 0
for value in numbers:
    # sum = sum + value
    sum += value

print(sum / len(numbers))

# exercise: given a list of number mixed with positive and negative
# create a new list only with positive value
numbers = [-1, 2, 1, -4]
new_numbers = []

for num in numbers:
    if num > 0:
        new_numbers.append(num)

print(new_numbers)

# while loop -> general usage
# for loop -> used with other thing
# use with list
for value in numbers:
    print(value)

# use with string
s = 'abcd'
for letter in s:
    print(letter)

# use with range
for i in range(10):
    print(i)



