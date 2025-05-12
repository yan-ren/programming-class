import turtle
import random


screen = turtle.Screen()

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

problems = int(screen.numinput('Input', 'How many math problem? (1-20)', minval=1, maxval=20))
operators = ['+', '-', 'x', '/']
score = 0

for i in range(problems):
    pen.clear()
    pen.goto(0, 100)

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operators)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == 'x':
        result = num1 * num2
    else:
        result = num1 / num2

    problem = f'{num1} {operation} {num2}'
    answer = screen.numinput('Answer', problem)

    if round(answer, 2) == round(result, 2):
        feedback = 'Correct!'
        score += 1
    else:
        feedback = 'Incorrect!'

    pen.write(feedback, align='center', font=('Arial', 20, 'bold'))

pen.clear()
pen.write(f'You got: {score}', align='center', font=('Arial', 20, 'bold'))
turtle.done()

'''
Password Validator
Implement a password validator that continuously asks the user to enter a password until it meets certain criteria 
(e.g., at least 8 characters long, contains both uppercase and lowercase letters, and has at least one number). 
The program should give feedback on what the entered password is missing if it doesn't meet the criteria.
'''