import pgzrun
import pgzero
import os
from pgzero.actor import Actor
from pgzero.rect import Rect
import random


screen: pgzero.screen.Screen
keyboard: pgzero.keyboard.Keyboard

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue.png')
ship.x = 370
ship.y = 550

box = Rect((20, 20), (100, 100))
background = Actor('sky_background.jpg')

def draw():
    screen.clear()
    background.draw()
    screen.draw.filled_rect(box, 'red')
    ship.draw()

score = 0

def update():
    global score
    if keyboard.right:
        ship.x += 2
    elif keyboard.left:
        ship.x -= 2
    elif keyboard.up:
        ship.y -= 2
    elif keyboard.down:
        ship.y += 2
    # if box.x < ship.x:
    #     box.x = box.x + 1
    # if box.x > ship.x:
    #     box.x = box.x - 1
    # if ship.colliderect(box):
    #     print('hit')
    if ship.colliderect(box):
        box.x = random.randint(0, WIDTH)
        box.y = random.randint(0, HEIGHT)
        score = score + 1
        print('Score', score)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()
