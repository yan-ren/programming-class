'''
given a list, e.g. l = [1, 2, 3]
create the reversed list e.g. [3, 2, 1]

given a list of string, e.g. ['abc', 'apple', 'cherry']
find the longest string, e.g. 'cherry'

Given a nested list [[1,2,3],[4,5,6],[7,8,9]], flatten it into [1,2,3,4,5,6,7,8,9]
'''

# l = [1, 2, 3]
#
# l_reverse = []
#
# for value in l:
#     l_reverse.insert(0, value)
#
# print(l_reverse)

# words = ['abc', 'apple', 'cherry']
# longest = ''
#
# for word in words:
#     if len(word) > len(longest):
#         longest = word
#
# print(longest)

# numbers = [[1,2,3],[4,5,6],[7,8,9]]
# new_numbers = []
#
# for num in numbers:
#     for v in num:
#         new_numbers.append(v)
#
# print(new_numbers)

import turtle
import random
import time


SCREEN_SIZE = 800
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)

turtle.delay(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.penup()

turtle.onkeypress(lambda: snake.setheading(90), "Up")
turtle.onkeypress(lambda: snake.setheading(-90), "Down")
turtle.onkeypress(lambda: snake.setheading(180), "Left")
turtle.onkeypress(lambda: snake.setheading(0), "Right")
turtle.listen()

food = turtle.Turtle()
food.shape('circle')
food.penup()
food.speed(0)
food.color('green')

food.goto(random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4), random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4))

score = 0

while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)
    if snake.distance(food) < 20:
        food.goto(random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4), random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4))
        snake.stamp()
        snake.stamp()
        score += 1
        print('Current score:', score)

    if snake.xcor() >= SCREEN_SIZE // 2 or snake.xcor() <= -SCREEN_SIZE // 2:
        break
    if snake.ycor() >= SCREEN_SIZE // 2 or snake.ycor() <= -SCREEN_SIZE // 2:
        break

    time.sleep(0.01)

'''
add score: add a variable to track score, when snake eats food, score +1
'''





