'''
Write a program asking user for three numbers, assume all those are different
How to find out the largest one?
'''
# first = int(input('Enter the first number:'))
# second = int(input('Enter the second number:'))
# third = int(input('Enter the third number:'))

# option 1
# if first > second > third ?
# if first > second and first > third:
#     print('First number is the largest')
# elif second > first and second > third:
#     print('Second number is the largest')
# else:
#     print('Third number is the largest')

# option 2: nested if statement: if statement inside if statement
# if first > second:
#     if first > third:
#         print('First is the largest')
#     else:
#         print('Third is the largest')
# else:
#     if second > third:
#         print('Second is the largest')
#     else:
#         print('Third is the largest')

import turtle
import random

wn = turtle.Screen()
wn.setup(800, 800)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

wn.bgcolor('red') # screen color


while True:
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    question = str(num1) + " + " + str(num2) + " = ?"
    answer = num1 + num2

    user_input = int(wn.textinput('Math question', question))
    # compare user_input with answer if correct, show something on the screen
    # if not correct, write failure message
    if user_input == answer:
        pen.write('Correct', align='center', font=('Arial', 24, "bold"))
    else:
        pen.color('orange')  # pen color
        pen.write('Wrong', align='center', font=('Arial', 24, "bold"))

turtle.done()

'''
follow up:
1. add more operations, e.g. multiplication, subtraction
2. show animation when answer is correct or wrong
3. add a score
'''