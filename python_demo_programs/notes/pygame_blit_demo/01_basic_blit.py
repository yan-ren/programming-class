"""
01_basic_blit.py
-----------------
The absolute minimum example of blitting an image in pygame.

CORE IDEA:
    blit() means "copy pixels from one Surface onto another Surface".
    Every image you load is a Surface. The screen is also a Surface.
    So "drawing an image" really means: screen.blit(image, position)

Run this file to see a single ship image sitting on a starfield background.
"""

import pygame
import sys

# 1. Always start with pygame.init() -- it sets up all pygame subsystems
pygame.init()

# 2. Create the display Surface. This is the "canvas" everything gets blitted onto.
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("01 - Basic Blit")

# 3. Load images from disk with pygame.image.load().
#    .convert() optimizes a background image (no transparency needed) for fast blitting.
#    .convert_alpha() keeps per-pixel transparency, which we need for the ship
#    (its corners are see-through, not a solid rectangle).
background = pygame.image.load("assets/background.png").convert()
player_image = pygame.image.load("assets/player.png").convert_alpha()

# 4. Pick a position for the ship. blit() takes a top-left (x, y) coordinate.
player_pos = (370, 270)

# 5. A tiny "game loop". Even a static image needs one, or the window closes instantly.
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- DRAWING ORDER MATTERS ---
    # Whatever you blit LAST is drawn ON TOP. Think of it like stacking
    # transparency sheets: background first, then everything else on top.
    screen.blit(background, (0, 0))       # 1st: fills the whole screen
    screen.blit(player_image, player_pos)  # 2nd: drawn on top of the background

    pygame.display.flip()  # show everything we just blitted
    clock.tick(60)          # cap the loop at 60 frames per second

pygame.quit()
sys.exit()
