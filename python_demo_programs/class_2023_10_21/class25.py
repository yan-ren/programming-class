import os

import pgzero
import pgzrun
import random

from pgzero.actor import Actor

screen: pgzero.screen.Screen
keyboard: pgzero.keyboard.Keyboard
os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 800
HEIGHT = 600

background = Actor('sky_background.jpg')

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

gem_red = Actor('gemred')
gem_red.x = random.randint(20, 780)
gem_red.y = 0

score = 0
game_over = False

def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]

def update():
    global score, game_over

    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

    gem.y = gem.y + 4 + score / 5
    if gem.y > 600:
        gem.y = 0
    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score = score + 1

    gem_red.y = gem_red.y + 4
    if gem_red.y > 600:
        gem_red.y = 0
    if gem_red.colliderect(ship):
        gem_red.x = random.randint(20, 780)
        gem_red.y = 0
        score = score - 1

    if score < 0:
        game_over = True

def draw():
    background.draw()
    if game_over:
        screen.draw.text('Game Over', (360, 300), color=(255,255,255), fontsize=60)
        screen.draw.text('Score: ' + str(score), (360, 350), color=(255,255,255), fontsize=60)
    else:
        gem_red.draw()
        gem.draw()
        ship.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line