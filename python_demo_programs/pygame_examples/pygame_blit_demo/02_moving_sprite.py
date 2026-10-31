"""
02_moving_sprite.py
--------------------
Builds on 01_basic_blit.py by MOVING the blitted image with the keyboard,
and introduces pygame.Rect, which is how pygame tracks an image's position
and size together.

CORE IDEA:
    image.get_rect() gives you a Rect the same size as the image, positioned
    at (0, 0). You then move that Rect around and blit() the image at
    rect.topleft (or just pass the rect itself -- blit accepts a Rect too).
    Using a Rect (instead of separate x, y numbers) makes movement,
    collision detection, and boundary-checking much easier later on.
"""

import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("02 - Moving Sprite (arrow keys)")

background = pygame.image.load("assets/background.png").convert()
player_image = pygame.image.load("assets/player.png").convert_alpha()

# get_rect() reads the image's width/height and wraps it in a Rect.
# .center lets us place it in the middle of the screen right away.
player_rect = player_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

PLAYER_SPEED = 5  # pixels moved per frame

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # pygame.key.get_pressed() returns the state of EVERY key, every frame.
    # This is the standard way to handle "held down" movement (as opposed to
    # single key-press events, which you'd catch in the event loop above).
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_rect.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_rect.y += PLAYER_SPEED

    # clamp() keeps the rect fully inside the screen boundary -- try removing
    # this line and see the ship fly off the edge.
    player_rect.clamp_ip(screen.get_rect())

    # --- draw order: background first, player on top ---
    screen.blit(background, (0, 0))
    screen.blit(player_image, player_rect)  # blit() accepts a Rect directly

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
