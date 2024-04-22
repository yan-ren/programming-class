import pygame

from python_demo_programs.class_2023_09_23.plane.enemy import Enemy

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
running = True

while running:
    for event in pygame.event.get():
        if event.type == ADD_ENEMY:
            new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.add(new_enemy)

    screen.fill(BLACK)
    for enemy in enemies:
        screen.blit(enemy.surf, enemy.rect)


    enemies.update()
    pygame.display.update()
    clock.tick(FPS)