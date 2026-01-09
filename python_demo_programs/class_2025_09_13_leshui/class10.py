import turtle
import random
import time

screen_size = 800
wn = turtle.Screen()
wn.setup(screen_size, screen_size)

turtle.delay(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.penup()

turtle.onkeypress(lambda: snake.setheading(90),'Up')
turtle.onkeypress(lambda: snake.setheading(-90), "Down")
turtle.onkeypress(lambda: snake.setheading(180), "Left")
turtle.onkeypress(lambda: snake.setheading(0), "Right")
turtle.listen()

food = turtle.Turtle(shape="circle")
food.penup()
food.speed(0)
food.color("green")
food.goto(random.randint(-screen_size//2, screen_size//2), random.randint(-screen_size//2, screen_size//2))

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

score = 0

colors = ['red', 'green', 'yellow']
current_color = random.choice(colors)

food.color(current_color)
while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)

    if snake.distance(food) < 20:
        food.goto(random.randint(-screen_size // 2, screen_size // 2),
                  random.randint(-screen_size // 2, screen_size // 2))
        score += 1
        pen.goto(350, 350)
        pen.clear()
        pen.write(score, align='center', font=('Ariel', 24, 'normal'))

        snake.color(current_color)
        current_color = random.choice(colors)
        food.color(current_color)
        snake.stamp()

    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 400 or snake.ycor() < -400:
        pen.goto(0, 0)
        pen.write('Game Over', align='center', font=('Ariel', 24, 'normal'))
        break

    time.sleep(0.01)


turtle.done()