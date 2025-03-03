# numbers = [1, 2, 4, 5, 6]
# numbers.append(10)
# print(numbers)

# loop through while loop
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1

# for index in range(len(numbers)):
    # print(numbers[index])
    # numbers[index] += 1

# for num in numbers:
#     # print(num)
#     num += 1
#
# print(numbers)

# given a list of numbers, calculate the average
# numbers = [1, 20, 12, 3, 4]
# s = 0
# for num in numbers:
#     s += num
#
# print(s / len(numbers))
#
# # python way
# print(sum(numbers) / len(numbers))

# given a list of numbers, find the max number
# numbers = [-1.5, -2, -3, -1, -4.5]
# max_number = numbers[0]
# # max_number = float('-inf')
# for num in numbers:
#     if num > max_number:
#         max_number = num
#
# print(max_number)

# numbers.sort(reverse=True)
# print(numbers[len(numbers) - 1])

# print(max(numbers))

'''
Exercise: given a list of number, find the second largest
'''

import random
import time
import turtle

screen = turtle.Screen()
screen.setup(600, 800)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

dice = [1, 2, 3, 4, 5, 6]
x = -60
y = 60
for i in range(3000):
    drawer.clear()
    value = random.choice(dice)

    # draw a square and write value inside the square
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    # draw square
    for _ in range(4):
        drawer.forward(50)
        drawer.right(90)
    # write number in the center
    drawer.penup()
    drawer.goto(x + 20, y - 35)
    drawer.write(value, align='center', font=("Arial", 20, "bold"))

    time.sleep(1)


turtle.done()


