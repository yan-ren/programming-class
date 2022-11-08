import random
import sys
import pygame

pygame.init()
WINDOWN_WIDTH = 1200
WINDOWN_HEIGHT = 800
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WINDOWN_WIDTH, WINDOWN_HEIGHT))

FPS = 60
clock = pygame.time.Clock()

cat = pygame.image.load('cat.png')
cat_x = WINDOWN_WIDTH / 2
cat_y = WINDOWN_HEIGHT / 2
cat_x_change = 0
cat_y_change = 0
mouse = pygame.image.load('mouse.png')
mouse_x = 0
mouse_y = 0
change_mouse = 0

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat_x_change = -10
            if event.key == pygame.K_RIGHT:
                cat_x_change = 10
            if event.key == pygame.K_UP:
                cat_y_change = -10
            if event.key == pygame.K_DOWN:
                cat_y_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                cat_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                cat_y_change = 0

    cat_x += cat_x_change
    cat_y += cat_y_change
    # left boarder
    if cat_x < 0:
        cat_x = 0
    # right boarder
    elif cat_x > WINDOWN_WIDTH - cat.get_width():
        cat_x = WINDOWN_WIDTH - cat.get_width()
    # up boarder / down boarder

    if change_mouse == FPS * 3:
        change_mouse = 0
        mouse_x = random.randint(0, WINDOWN_WIDTH - mouse.get_width())
        mouse_y = random.randint(0, WINDOWN_HEIGHT - mouse.get_height())
    else:
        change_mouse += 1

    screen.fill(WHITE)
    screen.blit(cat, (cat_x, cat_y))
    screen.blit(mouse, (mouse_x, mouse_y))
    pygame.display.update()
    clock.tick(FPS)