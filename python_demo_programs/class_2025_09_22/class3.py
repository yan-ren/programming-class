# name = input('What is your name:')
# print('Welcome', name)
#
# age = input('How old are you?')
# print('You are', age, 'years old')

import turtle

screen = turtle.Screen()
screen.setup(600, 800)

# name = screen.textinput('Name', 'Name')

pen = turtle.Turtle()
text = screen.textinput('Are you a student?', 'Are you a student?')
if text == 'Yes':
    pen.write('You are a student', font=('Arial', 24, "bold"))
else:
    pen.write('You are not a student', font=('Arial', 24, "bold"))



# pen.write('Hello' + name, font=('Arial', 24, "bold"))
#
# age = screen.textinput('How old are you', 'age')
# pen.penup()
# pen.goto(0, -100)
# pen.write('You are ' + age, font=('Arial', 24, "bold"))

'''
Today after class exercise:
Create Q&A program using the materials from today's class
'''
turtle.done()