
# j = 0
# while j < 4:
#     i = 0
#     while i < j:
#         print('*', end='')
#         i += 1
#     j += 1
#     print() # goto next line

'''
Snake game
1. keyboard control
2. create a snake and snake becomes longer when eats food
3. create food, food should move to other place when snake eats it
4. snake should not run outside of screen
optional:
5. add score tracking

out of the scope
snake runs into itself
'''
import turtle
import random
import time


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

score = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 360)
pen.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

# keyboard control
turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(-90), 'Down')
turtle.onkeypress(lambda: snake.setheading(180), 'Left')
turtle.onkeypress(lambda: snake.setheading(0), 'Right')
turtle.listen()


while True:
    snake.forward(2)
    snake.stamp()
    snake.clearstamps(1)

    if snake.distance(food) < 20:
        food.goto(random.randint(-200, 200), random.randint(-200, 200))
        snake.stamp()
        snake.stamp()
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

    if snake.xcor() > 400 or snake.xcor() < -400:
        break
    if snake.ycor() > 400 or snake.ycor() < -400:
        break

    time.sleep(0.01)


# Game Over message
snake.hideturtle()
food.hideturtle()
pen.goto(0, 0)
pen.write(f"Game Over! Final Score: {score}", align="center", font=("Arial", 28, "bold"))

'''
show the score on the screen, hint: create another turtle object, and use write function
1. show the score on the screen
2. when snake runs into the boarder, show Game Finish text and show the score
3. when game finish, press SPACE key to restart the game
'''