import time
import turtle
import math
import random
import winsound


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("8-bit SpaceWarS")
screen.bgpic("dp.gif")
screen.tracer(0)
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("missile.gif")

# player creation
player = turtle.Turtle()
player.color("blue")
player.speed(0)
player.shape("player.gif")
player.setheading(90)
player.penup()
player.goto(0, -250)
# player movement

player_speed = 20


def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -340:
        x = -340
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 340:
        x = 340
    player.setx(x)


# Enemy spawn
enemies = []
for i in range(7):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.speed(0)
    enemy.turtlesize(1.2, 1.2)
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.setheading(90)
    x = random.randint(-300, 300)
    y = random.randint(180, 260)  # 180.260
    enemy.goto(x, y)

enemyspeed = 1.8

# Bullet creation
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.speed(0)
bullet.shape("missile.gif")
bullet.turtlesize(0.5, 0.5)
bullet.penup()
bullet.hideturtle()
bullet.setheading(90)
bullet.goto(0, -240)

bulletspeed = 22
bulletstate = "Ready"


def firebullet():
    global bulletstate
    if bulletstate == "Ready":
        bulletstate = "Fire"
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

        x = player.xcor()
        y = player.ycor() + 20
        bullet.goto(x, y)
        bullet.showturtle()


Score = 0
# Draw score
scorepen = turtle.Turtle()
scorepen.pencolor("white")
scorepen.speed(0)
scorepen.up()
scorepen.setposition(-355, 280)
scorestring = "Score: %s" % Score
scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
scorepen.hideturtle()


# collision system
def collisionplay(a, b):

    distance = math.sqrt(
        abs(math.pow((a.xcor() - b.xcor()), 2) + math.pow((a.ycor() - b.ycor()), 2))
    )
    if distance < 25:
        return True
    else:
        return False


def collision(a, b):

    distance = math.sqrt(
        abs(math.pow((a.xcor() - b.xcor()), 2) + math.pow((a.ycor() - b.ycor()), 2))
    )
    if distance < 20:
        return True
    else:
        return False


# keybindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(firebullet, "space")
# main loop
while True:
    time.sleep(0.01)
    screen.update()
    # print(enemy.ycor())

    for enemy in enemies:
        # enemy movement
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        # Move enemy back and down
        if enemy.xcor() > 325:

            for j in enemies:
                y = j.ycor()
                y -= 25
                j.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -325:
            for j in enemies:
                y = j.ycor()
                y -= 25
                j.sety(y)
            enemyspeed *= -1

        if collisionplay(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "Ready"
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            bullet.setposition(0, -400)

            x = random.randint(-300, 300)
            y = random.randint(180, 280)
            enemy.setposition(x, y)
            Score += 10
            scorestring = "Score: %s" % Score
            scorepen.clear()
            scorepen.write(
                scorestring, False, align="left", font=("Arial", 14, "normal")
            )

        if collision(player, enemy):

            for e in enemies:
                e.hideturtle()
            player.hideturtle()

            winsound.PlaySound("gameover.wav", winsound.SND_ASYNC)
            print("GAME OVER")
            break

        if enemy.ycor() < -200:
            for j in enemies:
                j.hideturtle()
            player.hideturtle()

            print("GAME OVER")
            winsound.PlaySound("gameover.wav", winsound.SND_ASYNC)
            break

    # bullet movement
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    if bullet.ycor() > 150:
        bulletstate = "Ready"

    if bullet.ycor() > 300:
        bullet.hideturtle()
        bulletstate = "Ready"


delay = input()
