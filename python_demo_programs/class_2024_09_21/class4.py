# a = 123
# print(type(a))
# b = '123'
# print(type(b))

# a = 'abc123@##$!@$%'
# b = ''

# a = 1
# b = 1
# print(a + b)
#
# a = '1'
# b = 1
# print(a + b)

# a = 2
# b = 3
#
# c = a
# a = b
# b = c
#
# a = 'ABC'
# b = 'abc'
# if a == b:

# s = 'Arthur'
# print(s[0])
# print(len(s))
# print(s[len(s) - 1])
# print(s[-1])
# print(s[0:2])
# print(s)

import turtle

screen = turtle.Screen()
screen.setup(600, 800)

pen = turtle.Turtle()
pen.color('red')
name = screen.textinput('Input', 'Enter your name')

if name == 'bob':
    # draw the heart shape
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

    pen.write('Welcome Bob', font=('Arial', 18, 'normal'))
else:
    pen.write('Access denied', font=('Arial', 18, 'normal'))

turtle.done()

'''
ask user for 3 words, find the longest word
'''
first = input('Enter the first word:')
second = input('Enter the second word:')
third = input('Enter the third word:')

# if first > second and first > third:

# first_len, second_len, third_len = len(first), len(second), len(third)
#
# if first_len > second_len and first_len > third_len:
#     print(first)
# elif second_len > first_len and second_len > third_len:
#     print(second)
# else:
#     print(third)

