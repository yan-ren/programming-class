'''
if statement
looping: while loop, for loop
'''

'''
2. another coding exercise, print following pattern using while loop
*
**
***
****
***
**
*
'''

# line = 1
# while line <= 3:
#     start = 0
#     while start < line:
#         print('*', end='')
#         start += 1
#     print()
#     line += 1
#
# line = 1
# while line <= 4:
#     start = 0
#     while start < 5 - line:
#         print('*', end='')
#         start += 1
#     print()
#     line += 1

# how to sum all numbers under 100. e.g. 1+2+3+4+...+100
# using while loop and what's the result
# s = 0
# number = 1
# while number <= 100:
#     # print(number)
#     s = s + number
#     number += 1
#
# print(s)
# import turtle
#
# screen = turtle.Screen()
# screen.setup(600, 800)
#
# # n = int(input('Enter a number to calculate summation from 1 to n:'))
# n = screen.numinput('Input', 'Enter a number to calculate summation from 1 to n:')
# s = 0
# number = 1
# while number <= n:
#     s += number
#     number += 1
#
# pen = turtle.Turtle()
# pen.write('The result is ' + str(s), align='center', font=('Arial', 24, 'bold'))
#
# turtle.done()

'''
Build a simple calculator that can handle + - * /
'''
import turtle

screen = turtle.Screen()

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

while True:
    num1 = screen.numinput('Input', 'Enter the first number:')
    operator = screen.textinput('Input', 'Enter operator (+, -, *, /)')
    num2 = screen.numinput('Input', 'Enter the second number:')

    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: cannot divide by zero'
    elif operator == '^':
        result = num1 ** num2
    else:
        result = 'Error: not supported operator'

    pen.clear()
    pen.goto(0, 100)
    pen.write(str(num1) + operator + str(num2) + "=" + str(result), align='center', font=('Arial', 18, 'normal'))

'''
Add ^ operator to support calculating num1^num2
hint: in python we use ** to calculate power
'''
