'''
Overview

1. Continue work on Pygame library by building more complicated games/applications.
2. Discuss more advanced topics in Python programming, including object-oriented programming, data structures, and algorithms.
3. Discuss more CCC questions and solutions.
'''
'''
example 1

show minimum example of blitting an image in pygame

every image we load into pygame is a Surface. The screen is also a Surface.
'''
import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('assets/background.png').convert()
player_image = pygame.image.load('assets/player.png').convert_alpha()
player_rect = player_image.get_rect(center=(SCREEN_WIDTH //2, SCREEN_HEIGHT // 2))
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
    if keys[pygame.K_UP]:
        player_rect.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_rect.y += PLAYER_SPEED

    screen.blit(background, (0, 0))
    screen.blit(player_image, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()