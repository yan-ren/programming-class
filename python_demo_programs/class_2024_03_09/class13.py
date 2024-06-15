'''exercise
write a function which takes a list of string as input, return the longest string
'''

# def find_longest_str(words):
#     longest_str = ''
#     for word in words:
#         if word > longest_str:
#             longest_str = word
#
#     return longest_str
#
#
# words = ['aaa', 'aaaaa', 'aaaa']
# print(find_longest_str(words))

import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightblue')
WIDTH = 800
HEIGHT = 600

wn.setup(WIDTH, HEIGHT)

dots = []

current_score = 0

score = turtle.Turtle()
score.hideturtle()
score.penup()
score.color('black')
score.goto(0, 260)
score.write('Score:' + str(current_score), font=('Courier', 24, 'normal'))


def create_dot():
    dot = turtle.Turtle()
    dot.shape('circle')
    dot.color('red')
    dot.penup()
    dot.speed(0)
    return dot

def move_dot(dot):
    dot.goto(random.randint(-WIDTH//3, WIDTH//3), random.randint(-HEIGHT//3, HEIGHT//3))
    wn.ontimer(lambda: move_dot(dot), 3000)

def when_clicked(dot):
    dot.goto(random.randint(-WIDTH//3, WIDTH//3), random.randint(-HEIGHT//3, HEIGHT//3))

def handle_click(dot):
    dot.onclick(lambda x, y: when_clicked(dot))


for i in range(5):
    dots.append(create_dot())

for dot in dots:
    move_dot(dot)

for dot in dots:
    handle_click(dot)

turtle.done()