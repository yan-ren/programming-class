# name = input('Enter you name:')
# print('welcome', name)

import turtle
import time

screen = turtle.Screen()
screen.setup(600, 800)

color = screen.textinput('Enter a color:', 'Enter a color:')

t = turtle.Turtle()
t.color(color)
t.speed(6)
shape = screen.textinput('Enter a shape', 'Enter a shape:')

if shape == 'circle':
    t.circle(50)

time.sleep(1)

turtle.done()


'''
write a program ask user name, and age
then print if this user is adult or not
'''