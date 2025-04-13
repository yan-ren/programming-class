import turtle
import random
import time

'''
1. keyboard control
2. snake becomes longer when eats food
3. food move to other place when snake eats it
4. snake should not run outside of screen

more features to add:
1. score, showing the score on the screen
2. add another food, snake gets two scores
3. game should be able to restart when game finishes
'''
screen = turtle.Screen()
screen.setup(800, 800)
turtle.delay(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.penup()

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('green')
food.penup()
food.goto(random.randint(-200, 200), random.randint(-200, 200))

food2 = turtle.Turtle()
food2.speed(0)
food2.shape('circle')
food2.color('red')
food2.penup()
food2.goto(random.randint(-200, 200), random.randint(-200, 200))

# keyboard control
turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(-90), 'Down')
turtle.onkeypress(lambda: snake.setheading(180), 'Left')
turtle.onkeypress(lambda: snake.setheading(0), 'Right')
turtle.listen()

score = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 360)
# Score: 0
pen.write(f'Score: {score}', align='center', font=('Arial', 24, 'bold'))

while True:
    snake.goto(0, 0)
    snake.clear()
    snake.setheading(0)
    snake.showturtle()
    food.showturtle()
    food2.showturtle()
    food.goto(random.randint(-200, 200), random.randint(-200, 200))
    food2.goto(random.randint(-200, 200), random.randint(-200, 200))
    score = 0
    pen.clear()
    pen.write(f'Score: {score}', align='center', font=('Arial', 24, 'bold'))

    while True:
        snake.forward(2)
        snake.stamp()
        snake.clearstamps(1)

        if snake.distance(food) < 20:
            snake.stamp()
            food.goto(random.randint(-200, 200), random.randint(-200, 200))
            score += 1
            pen.clear()
            pen.write(f'Score: {score}', align='center', font=('Arial', 24, 'bold'))

        if snake.distance(food2) < 20:
            snake.stamp()
            snake.stamp()
            food2.goto(random.randint(-200, 200), random.randint(-200, 200))
            score += 2
            pen.clear()
            pen.write(f'Score: {score}', align='center', font=('Arial', 24, 'bold'))

        if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 400 or snake.ycor() < -400:
            break

        time.sleep(0.01)

'''
Homework:
1. improve the snake game, e.g. alternating the snake color / food color

2. another coding exercise, print following pattern using while loop
*
**
***
****
***
**
*
'''








