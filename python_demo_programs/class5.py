'''
exercise 1:
print squares of numbers from 1 to 10
1 4 9 16 25 36 49 64 81 100

exercise 2:
print odd numbers from 1 to 20

exercise 3:
Find the smallest number that is divisible by both 3 and 5 over 100
start from 100, find and print the first number greater than 100 that is divisible by both 3 and 5
'''

# # exercise 1
# i = 1
# while i <= 10:
#     print(i * i)
#     i += 1
#
# # exercise 2
# i = 1
# while i <= 20:
#     print(i)
#     i += 2
#
# # exercise 3
# i = 100
# running = True
#
# while running:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#         running = False
#     i += 1

# import turtle
# import random
# import time
#
#
# SCREEN_SIZE = 800
# wn = turtle.Screen()
# wn.setup(SCREEN_SIZE, SCREEN_SIZE)
# turtle.delay(0)
#
# snake = turtle.Turtle()
# snake.speed(0)
# snake.shape('square')
# snake.penup()
#
# turtle.onkeypress(lambda: snake.setheading(90), 'Up')
# turtle.onkeypress(lambda: snake.setheading(-90), 'Down')
# turtle.onkeypress(lambda: snake.setheading(180), 'Left')
# turtle.onkeypress(lambda: snake.setheading(0), 'Right')
# turtle.listen()
#
#
# food = turtle.Turtle()
# food.speed(0)
# food.shape('circle')
# food.penup()
# food.color('green')
# # -200 ~ 200
# food.goto(random.randint(-SCREEN_SIZE//4, SCREEN_SIZE//4), random.randint(-SCREEN_SIZE//4, SCREEN_SIZE//4))
#
# while True:
#     snake.forward(5)
#     snake.stamp()
#     snake.clearstamps(1)
#
#     if snake.distance(food) < 20:
#         food.goto(random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4), random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4))
#         snake.stamp()
#
#     time.sleep(0.01)
#
#
# turtle.done()


# break: jump outside of the loop immediately
i = 0
while i < 10:
    print(i)
    if i == 3:
        break
    i += 1

# continue: finish current iteration and go back to the beginning of the loop
i = 0
while i < 10:
    print(i)
    if i == 3:
        i += 1
        continue
    i += 1

'''
Exercise 1
Ask Until Positive Number
Ask the user to enter a number. If they enter a negative number, keep asking until they enter a positive one.
Hint: input()
'''
'''
Exercise 2
Counting Down
Ash the user to enter a positive number. Counting down from this positive number to zero
e.g. user enters 5
should print
5
4
3
2
1
0
'''









