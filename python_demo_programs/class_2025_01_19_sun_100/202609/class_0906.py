'''
example 2

blit multiple images onto the screen

pygame draws images in order.
Images drawn later appear on top of images drawn earlier.
'''
'''
example 3

use Rect to position images
'''
import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background = pygame.image.load('assets/background.png').convert()
# player_image = pygame.image.load('assets/player.png').convert_alpha()
# coin_image = pygame.image.load('assets/coin.png').convert_alpha()
#
# rect1 = player_image.get_rect(topleft = (50, 50))
# rect2 = player_image.get_rect(center=(400, 300))
# rect3 = player_image.get_rect(bottomright=(750, 550))
#
# coin_rect = coin_image.get_rect(center=(600, 300))
#
# clock = pygame.time.Clock()
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.blit(background, (0, 0))
#     screen.blit(coin_image, coin_rect)
#
#     screen.blit(player_image, rect1)
#     screen.blit(player_image, rect2)
#     screen.blit(player_image, rect3)
#
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()
# sys.exit()

'''
example 4 - move an image automatically
'''
# player_image = pygame.image.load('assets/player.png').convert_alpha()
# player_rect = player_image.get_rect(midleft=(0, 300))
#
# PLAYER_SPEED = 4
#
# clock = pygame.time.Clock()
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # move player
#     player_rect.x += PLAYER_SPEED
#     # if player leaves the screen move it back to the left side
#     if player_rect.x > SCREEN_WIDTH:
#         player_rect.right = 0
#     screen.fill('skyblue')
#     screen.blit(player_image, player_rect)
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()
# sys.exit()

'''
flip the player depending on direction
'''
player_right = pygame.image.load(
    'assets/player.png'
).convert_alpha()

player_left = pygame.transform.flip(
    player_right,
    True,
    False
)

player_rect = player_right.get_rect(center=(400, 300))
PLAYER_SPEED = 5

player_image = player_right

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
        player_image = player_left
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED
        player_image = player_right
    screen.fill('lightblue')
    screen.blit(player_image, player_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


