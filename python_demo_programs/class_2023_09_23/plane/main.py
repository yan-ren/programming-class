import pygame

from python_demo_programs.class_2023_09_23.plane.enemy import Enemy
from python_demo_programs.class_2023_09_23.plane.missile import Missile
from python_demo_programs.class_2023_09_23.plane.player import Player

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 125)
enemies = pygame.sprite.Group()

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

missiles = pygame.sprite.Group()

running = True

while running:
    for event in pygame.event.get():
        if event.type == ADD_ENEMY:
            new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.add(new_enemy)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            new_missle = Missile(SCREEN_WIDTH, player.rect.centerx, player.rect.centery)
            missiles.add(new_missle)

    screen.fill(BLACK)
    # draw missiles on screen
    for missile in missiles:
        screen.blit(missile.surf, missile.rect)

    # draw enemies on screen
    for enemy in enemies:
        screen.blit(enemy.surf, enemy.rect)

    # draw player on the screen
    screen.blit(player.surf, player.rect)

    # if pygame.sprite.spritecollideany(player, enemies):
    #     running = False

    # check collision between missiles and enemies
    # check two sprite group(list), if any object between two collides
    for enemy in enemies:
        if pygame.sprite.spritecollideany(enemy, missiles):
            enemy.kill()

    player.update(pygame.key.get_pressed())
    enemies.update()
    missiles.update()
    pygame.display.update()
    clock.tick(FPS)