import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('lightblue')
screen.title('Fun Math with Turtle!')

# Create a turtle for writing
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# Create a turtle for animations
anim = turtle.Turtle()
anim.shape('turtle')
anim.color('green')
anim.speed(2)

# Get username
name = screen.textinput('Input', "What's your name?")
pen.goto(0, 200)
pen.color('purple')
pen.write(f'Welcome, {name}!', align='center', font=('Comic Sans MS', 28, 'bold'))

# Move animation turtle in a circle
for _ in range(36):
    anim.forward(10)
    anim.right(10)

pen.clear()

problems = int(screen.numinput('Input', 'How many math problems? (1-5)', minval=1, maxval=5))

operations = ['+', '-', '*', '/']
score = 0
for _ in range(problems):
    pen.clear()
    pen.goto(0, 100)

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operations)

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

    if answer is not None and round(answer, 2) == round(result, 2):
        feedback = 'Correct'
        score += 1
    else:
        feedback = 'Wrong'

    pen.write(feedback, align='center', font=('Arial', 20, 'normal'))

pen.clear()
pen.write(f'You got {score}!', align='center', font=('Arial', 24, 'normal'))

turtle.done()

'''homework
draw a 2x2 square using python turtle
---------
|   |   |
---------
|   |   |
---------
'''
