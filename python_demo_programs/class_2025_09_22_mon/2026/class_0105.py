'''
- variable
    - int
    - float
    - boolean
    - string
- if statement
- loop
    - while
    - for
- list
'''
# number1 = int(input('Enter the first value:'))
# number2 = int(input('Enter the second value:'))
#
# print(number1, '+', number2, '=', number1 + number2)
# print(number1, '-', number2, '=', number1 - number2)

import turtle

screen = turtle.Screen()
screen.setup(600, 600)

number1 = int(screen.textinput('Enter the first value', 'Enter the first value'))
number2 = int(screen.textinput('Enter the second value', 'Enter the second value'))

pen = turtle.Turtle()
pen.penup()
# pen.write(str(number1) + '+' + str(number2) + '=' + str(number1 + number2), font=('Arial', 20, 'normal'))
# pen.goto(0, -50)
# pen.write(str(number1) + '-' + str(number2) + '=' + str(number1 - number2), font=('Arial', 20, 'normal'))
# pen.goto(0, -100)
# pen.write(str(number1) + '*' + str(number2) + '=' + str(number1 * number2), font=('Arial', 20, 'normal'))
# pen.goto(0, -150)
# pen.write(str(number1) + '/' + str(number2) + '=' + str(number1 / number2), font=('Arial', 20, 'normal'))

if number1 > 0 and number2 > 0:
    pen.write('All numbers are positive', font=('Arial', 20, 'normal'))
# continue: try to show which one is positive and which one is negative by adding more elif


turtle.done()

# a = 1
# b = 'hello'
# c = 2
# print(str(a) + b)
# print(a + c)