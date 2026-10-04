import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_image = pygame.image.load('assets/player.png').convert_alpha()

small_player_image = pygame.transform.scale(player_image, (50, 50))
large_player_image = pygame.transform.scale(player_image, (200, 200))

# example 3: different ways to position an image using Rect
# top left corner at x=50, y=50
rect1 = player_image.get_rect(topleft = (50, 50))

# centered at x=400, y=300
rect2 = player_image.get_rect(center=(400, 300))

# bottom-right corner at x=750, y=550
rect3 = player_image.get_rect(bottomright=(750, 550))

PLAYER_SPEED = 4

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    rect2.x += PLAYER_SPEED
    if rect2.left > SCREEN_WIDTH:
        rect2.right = 0

    screen.blit(player_image, rect1)
    screen.blit(player_image, rect2)
    screen.blit(player_image, rect3)
    screen.blit(small_player_image, (50, 100))
    screen.blit(large_player_image, (300, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()