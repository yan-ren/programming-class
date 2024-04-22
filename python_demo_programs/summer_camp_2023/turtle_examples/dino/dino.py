import turtle
import time
import keyboard

count = 0
dx = 0.3

img = "dino1.1.gif"
img1 = "dino1.1.gif"
img2 = "dino2.1.gif"
obj1 = "obs1.1.gif"
bgpic = "bgpic.PNG"

imglst = [img1, img2]

win = turtle.Screen()
win.bgpic(bgpic)
win.addshape(img)
win.addshape(img1)
win.addshape(img2)
win.addshape(obj1)
win.tracer(0)

obs1 = turtle.Turtle()
obs1.shape(obj1)
obs1.ht()
obs1.pu()
obs1.goto(420, 142)

dino = turtle
dino.lt(90)
dino.shape(img)
dino.pu()
dino.goto(-255, 142)
win.update()


def jump():
    for i in range(128):
        dino.sety(142 + i)
        win.update()
    time.sleep(0.1)
    dino.sety(170)
    win.update()
    dino.sety(142)


def obs1move():
    obs1x = obs1.xcor()
    obs1.setx(obs1x - dx)
    if obs1x < 300:
        obs1.st()
    if obs1x < -300:
        obs1.ht()
        obs1.setx(420)


while True:
    win.update()
    count = count + 1
    if count > 1:
        count = 0
    img = imglst[count]
    dino.shape(img)
    if keyboard.is_pressed("up") or keyboard.is_pressed("space"):
        jump()
    obs1move()