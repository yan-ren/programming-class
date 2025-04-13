'''
calculator using python turtle
- handle + - * /
- handle 0-9
'''
import turtle

screen = turtle.Screen()
screen.title('Turtle Calculator')

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

def draw_text(text, y):
    pen.goto(0, y)
    pen.clear()
    pen.write(text, align='center', font=('Arial', 18, 'normal'))

while True:
    operator = screen.textinput("Input", "Enter operator (+, -, *, /, sqrt) or 'exit' to quit:")
    if operator is None or operator == 'exit':
        break

    if operator == '^':
        base = screen.numinput('Input', 'Enter base number')
        exponent = screen.numinput('Input', 'Enter exponent')
        result = base ** exponent
        draw_text(f'{base} ^ {exponent} == {result}', 0)
        continue

    num1 = screen.numinput('Input', 'Enter first number:')
    num2 = screen.numinput('Input', 'Enter second number:')

    result = None

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: division by zero'
    else:
        result = 'Error: invalid operator'

    draw_text(f'{num1} {operator} {num2} = {result}', 0)

'''
Add "square" to the list of allowed operators in the prompt.

If the user types "square":

Ask for one number.

Multiply it by itself (use number * number).

Display the result using turtle like this:
5² = 25
'''