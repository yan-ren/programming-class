# import turtle
# import random
#
# from class_2025_02_22_sat_300.class11 import feedback
#
# screen = turtle.Screen()
#
# pen = turtle.Turtle()
# problems = int(screen.numinput('Input', 'How many math problem?', minval=1))
#
# operations = ['+', '-', '*', '/']
# score = 0
#
# for _ in range(problems):
#     num1 = random.randint(1, 100)
#     num2 = random.randint(1, 100)
#     op = random.choice(operations)
#
#     problem = f'{num1} {op} {num2}'
#     if op == '/':
#         result = num1 / num2
#     elif op == '+':
#         result = num1 + num2
#     elif op == '-':
#         result = num1 - num2
#     else:
#         result = num1 * num2
#
#     answer = screen.numinput('Answer', problem)
#     if round(answer, 2) == round(result, 2):
#         feedback = 'Correct'
#         score += 1
#     else:
#         feedback = 'Wrong'
#
#     pen.clear()
#     pen.write(feedback, align='center', font=('Arial', 24, 'normal'))
#
# pen.clear()
# pen.write(f'You got {score}', align='center', font=('Arial', 24, 'normal'))
# turtle.done()
line_number = 0
context = ''
with open('note.txt', 'r') as file:
    # context = file.read()
    # print(context)
    for line in file:
        print(line_number, line)
        line_number += 1
        context += line

print(context)

'''Exercise
List comprehension

Generate a list with following format
[1, -2, 9, -16, 25, -36, 49, -64, 81]
'''
