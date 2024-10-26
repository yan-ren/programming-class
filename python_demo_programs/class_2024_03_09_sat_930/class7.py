'''
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
food.goto(random.randint(int(-SCREEN_SIZE/4), SCREEN_SIZE/4), random.randint(-SCREEN_SIZE/4, SCREEN_SIZE/4))

pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.goto(0, 350)
pen.hideturtle()
score = 0
pen.write("Score: " + str(score), font=('Courier', 24, 'bold'))

while True:
    snake.forward(5)
    time.sleep(0.01)
    snake.stamp()
    snake.clearstamps(1)
    # boarder checking
    if (snake.xcor() < -SCREEN_SIZE/2 or snake.xcor() > SCREEN_SIZE/2
            or snake.ycor() < -SCREEN_SIZE/2
            or snake.ycor() > SCREEN_SIZE/2):
        break

    # snake eats food
    if snake.distance(food) < 20:
        food.goto(random.randint(-SCREEN_SIZE / 4, SCREEN_SIZE / 4), random.randint(-SCREEN_SIZE / 4, SCREEN_SIZE / 4))
        snake.stamp()
        snake.stamp()
        score = score + 1
        pen.clear()
        pen.write("Score: " + str(score), font=('Courier', 24, 'bold'))

turtle.done()
'''
'''
variable
if else
while loop - break - continue
list
for loop
'''
numbers = [2, 1, 4]
# print(numbers)
# numbers.append(3)
# print(numbers)
#
# print(numbers[2])
#
# del numbers[2]
# print(numbers)

# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index = index + 1

# find the sum of all numbers in the list
# index = 0
# sum = 0
# while index < len(numbers):
#     print(numbers[index])
#     sum = sum + numbers[index]
#     index = index + 1
#
# print('average:'+str(sum/len(numbers)))

# numbers = []
# index = 1
# while index <= 100:
#     numbers.append(index)
#     index = index + 1
#
# print(numbers)

# given a list of numbers, find the largest number
numbers = [2, 1, 5, 3, 4]

index = 0
max_value = 0
while index < len(numbers):
    if numbers[index] > max_value:
        max_value = numbers[index]

    index = index + 1

print(max_value)




# print(numbers[0])
# numbers[0] = 20
# print(numbers)
#
# names = ['tom', 'jerry']
