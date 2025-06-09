'''
"Garden Defender"
Concept:
A girl is protecting her magical garden. Cute bugs (like caterpillars or beetles) are trying to eat her flowers.
She moves up/down and throws water (or magic) to stop them. It's a mix of arcade-style reflexes and simple projectile logic.
'''
import os.path

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

'''
If your image is too large, use
https://imageresizer.com/
to resize

recommended image size:
player: 80x80
bug: 60x60
background: 800x600
'''
assets = os.path.join(os.path.dirname(__file__), 'assets')
player = pygame.image.load(os.path.join(assets, 'player.png'))
bug = pygame.image.load(os.path.join(assets, 'bug.png'))
water = pygame.image.load(os.path.join(assets, 'water.png'))
background = pygame.image.load(os.path.join(assets, 'background.jpg'))

