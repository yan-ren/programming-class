"""
03_multiple_images_and_transforms.py
-------------------------------------
Introduces:
  - Blitting MANY images in one frame (a list of enemies)
  - Draw order / layering with several different image types
  - pygame.transform.scale()  -> resizing an image before blitting
  - pygame.transform.rotate() -> rotating an image before blitting
  - Adjusting transparency with set_alpha()

CORE IDEA:
    You never "move" or "resize" pixels that are already on screen.
    Instead, each frame you: clear the screen (blit background),
    then blit fresh, freshly-transformed copies of your images at
    their current positions. This full-redraw-every-frame approach
    is the standard pygame pattern.
"""

import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("03 - Multiple Images & Transforms")

background = pygame.image.load("assets/background.png").convert()
player_image = pygame.image.load("assets/player.png").convert_alpha()
enemy_image = pygame.image.load("assets/enemy.png").convert_alpha()
coin_image = pygame.image.load("assets/coin.png").convert_alpha()

player_rect = player_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80))

# --- Multiple enemies: store each one's position in a list of Rects ---
random.seed(1)
enemy_rects = [
    enemy_image.get_rect(topleft=(random.randint(0, SCREEN_WIDTH - 50), random.randint(20, 200)))
    for _ in range(6)
]
ENEMY_SPEED = 2

# --- A coin that we will rotate every frame to fake a "spinning coin" ---
coin_center = (120, 300)
coin_angle = 0

# --- A bigger, scaled-up copy of the player image, just to demonstrate scale() ---
# transform.scale(surface, (new_width, new_height)) returns a NEW surface;
# it does not modify the original.
big_player_image = pygame.transform.scale(player_image, (120, 120))

PLAYER_SPEED = 5
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED
    player_rect.clamp_ip(screen.get_rect())

    # Move each enemy down; when it reaches the bottom, send it back to the top.
    for rect in enemy_rects:
        rect.y += ENEMY_SPEED
        if rect.top > SCREEN_HEIGHT:
            rect.y = -40
            rect.x = random.randint(0, SCREEN_WIDTH - rect.width)

    # Spin the coin: rotate() returns a NEW rotated surface each frame.
    # Rotating changes the surface's size slightly, so we re-fetch a rect
    # centered on the same spot, otherwise the coin would "drift" as it spins.
    coin_angle = (coin_angle + 3) % 360
    rotated_coin = pygame.transform.rotate(coin_image, coin_angle)
    rotated_coin_rect = rotated_coin.get_rect(center=coin_center)

    # --- DRAW ORDER (back to front) ---
    screen.blit(background, (0, 0))                 # 1. background
    for rect in enemy_rects:                        # 2. enemies
        screen.blit(enemy_image, rect)
    screen.blit(rotated_coin, rotated_coin_rect)     # 3. spinning coin
    screen.blit(player_image, player_rect)           # 4. player

    # 5. A translucent "preview" of the big player image in the corner,
    #    demonstrating set_alpha() (0 = fully see-through, 255 = fully solid).
    big_player_image.set_alpha(120)
    screen.blit(big_player_image, (SCREEN_WIDTH - 130, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
