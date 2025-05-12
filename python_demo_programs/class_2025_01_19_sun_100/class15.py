'''
more about for loop
'''
# for i in range(10):

# s = 'abcdefghi'
#
# for ch in s:
#     print(ch)

'''exercise
given a string s, count how many vowels inside
'''
# s = input('Enter a word:')
# count = 0
#
# for ch in s:
#     if ch in 'aeiou':
#         count += 1
#     # if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#     #     count += 1
#
# print(count)

# break: exit from the loop
# i= 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
#
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# continue: finish current loop, go back to the loop header, check loop condition again
# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1

import turtle
import random

screen = turtle.Screen()
screen.bgcolor('lightblue')
screen.title('Math Quiz')

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

problems = int(screen.numinput('Input', 'How many math problems? (1-5)', minval=1, maxval=5))
operators = ['+', '-', '*', '/']
score = 0

for i in range(problems):
    pen.clear()

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operators)

    if operation == '/':
        result = num1 / num2
    elif operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    problem = f'{num1} {operation} {num2}'
    answer = screen.numinput('Answer', problem)

    # compare the answer with result
    if round(answer, 2) == round(result, 2):
        feedback = 'Correct!'
        score += 1
    else:
        feedback = 'Wrong!'
    pen.write(feedback, align='center', font=('Arial', 20, 'normal'))

pen.clear()
pen.write(f'You got {score}!', align='center', font=('Arial', 24, 'normal'))

turtle.done()

'''
Password Validator
Implement a password validator that continuously asks the user to enter a password until it meets certain criteria 
(e.g., at least 8 characters long, contains both uppercase and lowercase letters, and has at least one number). 
The program should give feedback on what the entered password is missing if it doesn't meet the criteria.
'''