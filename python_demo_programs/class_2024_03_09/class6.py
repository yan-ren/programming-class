# text = input('enter a word for palindrome checking:')
#
# index = 0
# is_palindrome = True
# while index < len(text) / 2:
#     if text[index] != text[len(text) - 1 - index]:
#         is_palindrome = False
#         break
#     index = index + 1
#
# if is_palindrome:
#     print('is palindrome')
# else:
#     print('is not palindrome')

# prime number
# number = int(input('enter a number:'))
# divisor = 2
# is_prime = True
# while divisor < number:
#     if number % divisor == 0:
#         is_prime = False
#     divisor += 1
#
# if is_prime:
#     print('is prime')
# else:
#     print('not prime')

import turtle
import random
import time


SCREEN_SIZE = 800
window = turtle.Screen()
window.setup(SCREEN_SIZE, SCREEN_SIZE)

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.penup()

turtle.onkeypress(lambda: snake.setheading(90), "Up")
turtle.onkeypress(lambda: snake.setheading(-90), "Down")
turtle.onkeypress(lambda: snake.setheading(180), "Left")
turtle.onkeypress(lambda: snake.setheading(0), "Right")
turtle.listen()

food = turtle.Turtle(shape='circle')
food.penup()
food.speed(0)
food.color('green')
food.goto(random.randint(-SCREEN_SIZE/4, SCREEN_SIZE/4), random.randint(-SCREEN_SIZE/4, SCREEN_SIZE/4))

while True:
    snake.forward(5)
    time.sleep(0.01)

    if snake.distance(food) < 20:
        food.goto(random.randint(-SCREEN_SIZE / 4, SCREEN_SIZE / 4), random.randint(-SCREEN_SIZE / 4, SCREEN_SIZE / 4))

turtle.done()
