import pygame
import sys

'''
example 1

show minimum example of blitting an image in pygame

every image we load into pygame is a Surface, The screen is also Surface.
'''

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('assets/background.png').convert()
player_image = pygame.image.load('assets/player.png').convert_alpha()
coin_image = pygame.image.load('assets/coin.png').convert_alpha()

player_rect = player_image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
coin_rect = coin_image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    screen.blit(background, (0, 0))
    screen.blit(player_image, player_rect)
    screen.blit(coin_image, coin_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
