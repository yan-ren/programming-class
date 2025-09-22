'''
Ask for a student's score (0–100). Print their grade:
A: 90+
B: 80–89
C: 70–79
D: 60–69
F: below 60
'''

# score = int(input("Enter your score: "))
#
# if score > 90:
#     print('A')
# elif 80 < score <= 89:
#     print('B')
# elif 70 < score <= 79:
#     print('C')
# elif 60 < score <= 69:
#     print('D')
# else:
#     print('F')

# input a single letter and check if it's a vowel (a, e, i, o, u)
# letter = input('Enter a letter:')
# if letter == 'a' or letter == 'e' or letter == 'o' or letter == 'u' or letter == 'i':
#     print('vowel')
# else:
#     print('consonant')

'''
Input a year and check if it's a leap year using:
- Divisible by 4
- Not divisible by 100 unless also divisible by 400
'''
# number = int(input('Enter a year:'))
# if number % 4 == 0:
#     print('Leap year')
# elif number % 100 == 0 and number % 400 == 0:
#     print('Leap year')
# else:
#     print('Not leap year')

import turtle

screen = turtle.Screen()

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.write("Welcome to Calculator!", align="center", font=("Arial", 16, "bold"))

num1 = float(input('Enter the first number:'))
op = input('Enter operation: + - * /')
num2 = float(input('Enter the second number:'))

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 == 0:
        result = 'error: cannot be divided by zero'
    else:
        result = num1 / num2
else:
    result = 'invalid operator'

pen.clear()
pen.write(result, align='center', font=('Arial', 18, 'bold'))

turtle.done()