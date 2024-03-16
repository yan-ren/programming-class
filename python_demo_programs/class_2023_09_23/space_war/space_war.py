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
    enemies.append(enemy)

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

enemy_xchange = 2

while True:
    time.sleep(0.01)
    screen.update()

    # missile move
    if missile.ycor() < 300:
        missile.sety(missile.ycor() + 20)
    else:
        missile.hideturtle()
        missile_state = 'Ready'

    for enemy in enemies:
        enemy.setx(enemy.xcor() + enemy_xchange)

    enemy_xchange *= -1


# turtle.done()
