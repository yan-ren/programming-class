'''
For exercise
'''

# numbers = [[1, 2, 3], [2, 1, 2], [3, 5]]

# create a list with largest number from each sub-list
# result = [3, 2, 5]
# result = []
#
# for sub in numbers:
#     max = sub[0]
#     for num in sub:
#         if num > max:
#             max = num
#
#     result.append(max)
#
# print(result)

'''
Given a string with letters, find out which letters showed up the most
assume there is only one
e.g. s = 'abaacdebbb'
b is the most frequent letter
Hint: count
'''
# s = 'abaacdebbb'
# most_frequent_letter = ''
# most_frequent_count = 0
#
# for letter in s:
#     if s.count(letter) > most_frequent_count:
#         most_frequent_count = s.count(letter)
#         most_frequent_letter = s.count(letter)
#
# print(most_frequent_letter)

import turtle
import random


screen = turtle.Screen()
screen.setup(width=700, height=450)
screen.bgcolor('honeydew')

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, 0)

colors = ["red", "blue", "green", "orange", "purple"]

START_X = -300
FINISH_X = 300

# FOR LOOP 1: make one racing turtle for each color
racers = []
for i in range(len(colors)):
    racer = turtle.Turtle(shape='turtle')
    racer.color(colors[i])
    racer.penup()
    racer.goto(START_X, 150 - i * 60)
    racers.append(racer)

# FOR LOOP 2: run the race
finished = False
while not finished:
    for racer in racers:
        racer.forward(random.randint(1, 20))
        if racer.xcor() >= FINISH_X:
            finished = True
            break

# FOR LOOP 3: find and announce the winner
winner = None
for racer in racers:
    if racer.xcor() >= FINISH_X:
        winner = racer
        break

# print(f'The winner is {winner.pencolor()}')
# show the winner on the screen
text.write(
    f'{winner.pencolor()} wins!',
    align='center',
    font=('Arial', 36, 'bold')
)

screen.exitonclick()

'''
add a countdown ('3...2...1...GO!) before the race starts using time.sleep()
'''