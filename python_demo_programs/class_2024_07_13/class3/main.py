import pygame

from python_demo_programs.class_2024_07_13.class3.enemy import Enemy
from python_demo_programs.class_2024_07_13.class3.missile import Missile
from python_demo_programs.class_2024_07_13.class3.plane import Plane

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

FPS = 60

# create a timer to add enemy automatically
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 125)

enemies = pygame.sprite.Group()
plane = Plane(SCREEN_WIDTH, SCREEN_HEIGHT)
running = True

missiles = pygame.sprite.Group()


while running:
    for event in pygame.event.get():
        if event.type == ADD_ENEMY:
            new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.add(new_enemy)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            new_missile = Missile(SCREEN_WIDTH, plane.rect.centerx, plane.rect.centery)
            missiles.add(new_missile)

    screen.fill((0, 0, 0))
    # draw missiles on screen
    for missile in missiles:
        screen.blit(missile.surf, missile.rect)

    # draw enemies on the screen
    for enemy in enemies:
        screen.blit(enemy.surf, enemy.rect)

    # draw plane on the screen
    screen.blit(plane.surf, plane.rect)
    plane.update(pygame.key.get_pressed())

    # check collision between missiles and enemies
    for enemy in enemies:
        if pygame.sprite.spritecollideany(enemy, missiles):
            enemy.kill()

    if pygame.sprite.spritecollideany(plane, enemies):
        running = False

    enemies.update()
    missiles.update()
    pygame.display.update()
    clock.tick(FPS)


