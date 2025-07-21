'''
- nested loop
- 2d list

- snake game using turtle module
'''
# i = 1
#
# while i <= 100:
#     number = i
#     result = 'Prime'
#     j = 2
#     while j < number:
#         if number % j == 0:
#             result = "Not Prime"
#             break
#         j += 1
#     print(result)
#     i += 1

'''
***
***
***
'''
for row in range(3):
    for col in range(3):
        print('*', end='')
    print()

'''
*
**
***
****
*****
******
'''

'''
Print multiplication table using nested loop
'''

'''
while vs for
while: general usage, when iteration of the loop is not clear
for: always used with other thing, the iteration of the for loop is clear

range(10) -> 0, 1, ..., 9
range(1, 10) -> 1, 2, 3, ..., 9
range(1, 10, 2) -> 1, 3, 5, .., 9
'''
# for i in range(10, 0, -1):
#     print(i)
#
# for ch in 'abcdef123':
#
# for num in [1, 2, 3, 4]:

# numbers = [1, 2, 3, 4]
# # for num in numbers:
# #     num += 1
# #
#
# for i in range(len(numbers)):
#     numbers[i] += 1
#
# print(numbers)

'''
Snake game using turtle module
'''
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

def go_up():
    snake.setheading(90)

def go_down():
    snake.setheading(-90)

def go_left():
    snake.setheading(180)

def go_right():
    snake.setheading(0)

turtle.onkeypress(go_up, 'Up')
turtle.onkeypress(go_down, 'Down')
turtle.onkeypress(go_left, 'Left')
turtle.onkeypress(go_right, 'Right')
turtle.listen()

food = turtle.Turtle()
food.penup()
food.speed(0)
food.color('green')
food.shape('circle')
food.goto(random.randint(-SCREEN_SIZE//4, SCREEN_SIZE//4), random.randint(-SCREEN_SIZE//4, SCREEN_SIZE//4))

score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(350, 350)

while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)

    if snake.distance(food) < 20:
        food.goto(random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4),
                  random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4))
        snake.stamp()
        score += 1
        pen.clear()
        pen.write(score, align='center', font=('Arial', 24, 'normal'))

    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 400 or snake.ycor() < -400:
        break

    time.sleep(0.01)
