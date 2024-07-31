import pygame

from python_demo_programs.class_2024_07_13.class3.enemy import Enemy

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

running = True

while running:
    for event in pygame.event.get():
        if event.type == ADD_ENEMY:
            new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.add(new_enemy)

    screen.fill((0, 0, 0))
    # draw enemies on screen
    for enemy in enemies:
        screen.blit(enemy.surf, enemy.rect)

    enemies.update()
    pygame.display.update()
    clock.tick(FPS)


