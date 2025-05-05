import turtle
import random

screen = turtle.Screen()

pen = turtle.Turtle()
problems = int(screen.numinput('Input', 'How many math problems? (1-5)', minval=1, maxval=5))

operations = ['+', '-', '*', '/']
score = 0
for _ in range(problems):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(operations)

    problem = f'{num1} {op} {num2}'
    if op == '/':
        result = num1 / num2
    elif op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    answer = screen.numinput('Answer', problem)
    if round(answer, 2) == round(result, 2):
        feedback = 'Correct'
        score += 10
    else:
        feedback = 'Wrong'
    pen.write(feedback, align='center', font=('Arial', 24, 'normal'))

pen.clear()
pen.write(f'You got {score}', align='center', font=('Arial', 24, 'normal'))
turtle.done()

'''Favorite Fruits
Ask the user to enter favorite fruits and if enter 'exit' then stop

store them in a list, then print the list.

'''