# age = int(input('How old are you:'))
# print('You entered:', age)

# print the type of age variable
# print(type(age))

# conditional
# if 18 <= age <= 65:
#     print('you are young adult')
# elif age > 65:
#     print('you can retire')
# else:
#     print('under age')

# ask people for a number, tell them it's positive or negative or zero
# number = int(input('Enter a number:'))
#
# # nested if statement
# if number > 0:
#     print('positive')
#     if number % 2 == 0:
#         print('even')
#     else:
#         print('odd')
# elif number < 0:
#     print('negative')
# else:
#     print('zero')

# exercise 1: ask user for two numbers, determine which is bigger
# exercise 2: ask user for three numbers, determine the biggest one
import turtle
import random
import time

pen = turtle.Turtle()
pen.speed(0)
pen.write('Welcome', align='center', font=('Arial', 20, 'bold'))
num = random.randint(1, 10)

if num <= 3:
    pen.color('red')
    pen.forward(100)
elif num <= 6:
    pen.color('blue')
    pen.forward(100)
    pen.right(120)
    pen.forward(100)
    pen.right(120)
    pen.forward(100)
    pen.right(120)
elif num <= 9:
    pen.color('green')
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
else:
    pen.circle(50)

turtle.done()
