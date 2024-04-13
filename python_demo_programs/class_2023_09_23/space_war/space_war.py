import random
import time
import turtle
import winsound

screen = turtle.Screen()
# screen.bgcolor('black')
screen.bgpic('dp.gif')
turtle.register_shape('player.gif')
turtle.register_shape('enemy.gif')
turtle.register_shape('missile.gif')

# player creation
player = turtle.Turtle()
player.speed(0)
player.shape('player.gif')
player.setheading(90)
player.penup()
player.goto(0, -250)

# Missile creation
missile = turtle.Turtle()
missile.speed(0)
missile.shape('missile.gif')
missile.turtlesize(0.5, 0.5)
missile.penup()
missile.hideturtle()
missile.setheading(90)

# Enemy creation
enemies = []
for i in range(6):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape('enemy.gif')
    enemy.turtlesize(1.2, 1.2)
    enemy.penup()
    enemy.setheading(90)
    enemy.goto(random.randint(-300, 300), random.randint(180, 260))
    enemy.move_speed = 10
    enemies.append(enemy)

writer = turtle.Turtle()
writer.pencolor('white')
writer.speed(0)
writer.penup()
writer.setposition(-355, 280)
writer.hideturtle()

def move_left():
    x = player.xcor()
    x -= 20
    if x < -340:
        x = -340
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 340:
        x = 340
    player.setx(x)


missile_state = 'Ready'
def fire_missile():
    global missile_state
    if missile_state == 'Ready':
        missile_state = 'Fire'
        winsound.PlaySound('laser.wav', winsound.SND_ASYNC)
        missile.goto(player.xcor(), player.ycor())
        missile.showturtle()


turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')
turtle.onkeypress(fire_missile, 'space')
turtle.listen()

score = 0

while True:
    time.sleep(0.01)
    screen.update()

    writer.clear()
    writer.write("Score: " + str(score), False, align='left', font=('Arial', 14, 'normal'))
    # missile move
    if missile_state == 'Fire' and missile.ycor() < 300:
        missile.sety(missile.ycor() + 20)
    else:
        missile.hideturtle()
        missile_state = 'Ready'

    # enemies moving down
    for enemy in enemies:
        enemy.setx(enemy.xcor() + enemy.move_speed)
        if enemy.xcor() > 325 or enemy.xcor() < -325:
            enemy.sety(enemy.ycor() - 25)
            enemy.move_speed *= -1

        # collide with missile
        if missile_state == 'Fire' and missile.distance(enemy) < 20:
            enemy.setposition(random.randint(-300, 300), random.randint(180, 280))

        # collide with player
        if enemy.distance(player) < 20:
            winsound.PlaySound('gameover.wav', winsound.SND_ASYNC)
            break

        # enemy touches the bottom
        if enemy.ycor() < -200:
            winsound.PlaySound('gameover.wav', winsound.SND_ASYNC)
            break




# turtle.done()
