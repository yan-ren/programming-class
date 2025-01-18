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
    color = ['red', 'yellow', 'blue']
    dot = turtle.Turtle()
    dot.shape('circle')
    dot.color(random.choice(color))
    dot.penup()
    dot.speed(0)
    return dot

def move_dot(dot):
    dot.goto(random.randint(-WIDTH//3, WIDTH//3), random.randint(-HEIGHT//3, HEIGHT//3))
    wn.ontimer(lambda: move_dot(dot), 3000)

def when_clicked(dot):
    global current_score
    dot.goto(random.randint(-WIDTH//3, WIDTH//3), random.randint(-HEIGHT//3, HEIGHT//3))
    # current_score += 1
    if dot.pencolor() == 'red':
        current_score += 1
    if dot.pencolor() == 'yellow':
        current_score += 2
    if dot.pencolor() == 'blue':
        current_score -= 1

    score.clear()
    score.write('Score:' + str(current_score), font=('Courier', 24, 'normal'))

    if current_score < 0:
        score.clear()
        score.write('Game Over', font=('Courier', 24, 'normal'))

def handle_click(dot):
    dot.onclick(lambda x, y: when_clicked(dot))


for i in range(5):
    dots.append(create_dot())

for dot in dots:
    move_dot(dot)

for dot in dots:
    handle_click(dot)

turtle.done()

'''
Exercise: 
1. Add more dots, each dot represents different score
2. Some dots may get your score lower, if score is < 0. Game over 
'''