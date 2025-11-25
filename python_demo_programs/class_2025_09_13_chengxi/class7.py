import turtle
import random
import time


SCREEN_SIZE = 800
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)

turtle.delay(0)
# one turtle object to draw snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.penup()

turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(-90), "Down")
turtle.onkeypress(lambda: snake.setheading(180), "Left")
turtle.onkeypress(lambda: snake.setheading(0), "Right")

food = turtle.Turtle(shape='circle')
food.penup()
food.speed(0)
food.color('green')
food.goto(random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4), random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4))

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(100, 100)

score = 0

speed = turtle.numinput("Difficulty", "1 = slow, 2 = normal, 3 = fast", 2)
if speed == 1:
    delay = 0.08
elif speed == 2:
    delay = 0.04
else:
    delay = 0.02

paused = False

def toggle_pause():
    global paused
    paused = not paused

wn.onkeypress(toggle_pause, "space")
turtle.listen()

while True:
    if paused:
        time.sleep(delay)
        continue

    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)

    if snake.distance(food) < 20:
        food.goto(random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4),
                  random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4))
        snake.stamp()
        snake.stamp()
        score += 1
        pen.clear()
        pen.write('Score: ' + str(score), align='center', font=(24, 'Arial', 'normal'))

    if snake.xcor() > SCREEN_SIZE / 2 or snake.xcor() < - SCREEN_SIZE / 2 or snake.ycor() > SCREEN_SIZE / 2 or snake.ycor() < -SCREEN_SIZE / 2:
        pen.goto(0, 0)
        pen.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
        break

    time.sleep(delay)