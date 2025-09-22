'''
Given a nested list [[1,2,3],[4,5,6],[7,8,9]], flatten it into [1,2,3,4,5,6,7,8,9]
'''

# numbers = [[1,2,3],[4,5,6],[7,8,9]]
# new_numbers = []
#
# for values in numbers:
#     for num in values:
#         new_numbers.append(num)
#
# print(new_numbers)

'''
dictionary

key-value pair
'''

# ages = {
#     'Alice': 9,
#     'Bob': 8
# }
#
# ages['Chris'] = 10
# print(ages)
#
# del ages['Alice']
# print(ages)
#
# ages['Bob'] = 10
# print(ages)
#
# if 'Bob' in ages:
#     print('exists')
#
# # loop key-value same time
# for name, age in ages.items():
#     print(name, age)
#
# # loop key only
# for name in ages:
#     print(name)
#
# # loop value only
# for age in ages.values():
#     print(age)

'''
Build a simple turtle game where a player controls a turtle to collect food items (e.g. apple, banana, orange, etc)
we use a dictionary to store the score of each type of food
'''


import turtle
import random
import time

# setup screen
screen = turtle.Screen()
screen.bgcolor('lightblue')
screen.setup(600, 600)

# create player turtle
player = turtle.Turtle()
player.shape('turtle')
player.penup()
player.speed(0)

# create food turtle
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-280, 280), random.randint(-280, 280))

score = {"apple": 0, "banana": 0}
speed = 10

def go_up():
    player.setheading(90)
    player.forward(speed)

def go_down():
    player.setheading(270)
    player.forward(speed)

def go_left():
    player.setheading(180)
    player.forward(speed)

def go_right():
    player.setheading(0)
    player.forward(speed)

screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, 'Down')
screen.onkeypress(go_left, 'Left')
screen.onkeypress(go_right, 'Right')
screen.listen()

while True:
    if player.distance(food) < 20:
        food_type = random.choice(['apple', 'banana'])
        score[food_type] += 1 # update the dictionary value
        print('Collected:', food_type) # follow up, instead of print, show the text on screen
        print('Score:', score)

        food.goto(random.randint(-280, 280), random.randint(-280, 280))

    screen.update()
    time.sleep(0.05)

'''
ages = {
    'Alice': 20,
    'Bob': 10,
    'Cindy': 21
}

find the name who is the oldest
'''
# ages = {
#     'Alice': 20,
#     'Bob': 10,
#     'Cindy': 21
# }
# name = ''
# older = 0
#
# for key, value in ages.items():
#     if value > older:
#         older = value
#         name = key
#
# print(name)