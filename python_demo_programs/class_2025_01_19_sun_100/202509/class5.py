'''
write a function that takes a list of numbers as input, and return a new list with only positive values

e.g.

input: [1, -2, 3, -1]
output: [1, 3]
'''
# def filter_positive(numbers):
#     result = []
#     for num in numbers:
#         if num > 0:
#             result.append(num)
#
#     return result
#
# print(filter_positive([1, 2, -1, -2]))
#
#
# def calculation(a, b):
#     sum = a + b
#     sub = a - b
#
#     return sum, sub
#
# print(calculation(1, 2))

import turtle

screen = turtle.Screen()
screen.title('Turtle Calculator')
screen.setup(500, 500)
screen.tracer(0)

# 2D list
buttons = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['C', '0', '=', '/']
]

current_input = ''
result = None

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

def draw_button(x, y, text):
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor('lightgrey')
    pen.begin_fill()
    for _ in range(2):
        pen.forward(80)
        pen.right(90)
        pen.forward(60)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(x + 30, y - 40)
    pen.write(text, align='center', font=('Arial', 18, 'bold'))


def draw_calculator():
    pen.clear()
    y = 100
    for row in buttons:
        x = -150
        for label in row:
            draw_button(x, y, label)
            x += 80
        y -= 70
    screen.update()

def on_click(x, y):
    global current_input

    col = int((x + 160) // 80)
    row = int((180 - y) // 70) - 1

    if 0 <= row < 4 and 0 <= col < 4:
        label = buttons[row][col]
        handle_input(label)

def handle_input(label):
    global current_input

    if label == 'C':
        current_input = ""
        print('Cleared')
    elif label == '=':
        result = evaluate_expression(current_input)
        print(f"{current_input} = {result}")
        current_input = ""
    else:
        current_input += label
        print("Current input:", current_input)


def evaluate_expression(expression):
    return str(eval(expression))


draw_calculator()
screen.onclick(on_click)
turtle.done()

'''homework
Solve following question by writing a function
1. given a list of numbers, find how many positive value and negative values, return those result
e.g.
[1, 2, -1, 0, -4]
return 2, 2

2. write a function that takes two list of number as input, merge them into a single list without duplicates
e.g.
input:
[1, 2, 3]
[2, 3, 4]
return
[1, 2, 3, 4]
'''