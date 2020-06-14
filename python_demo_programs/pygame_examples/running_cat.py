import pygame, os

pygame.init()
screen = pygame.display.set_mode((800, 600))
# R G B value for color, R-Red, G-Green, B-Blue
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
clock = pygame.time.Clock()
# cat = pygame.image.load('/home/yan.ren/github.com/ProgrammingClass/python_demo_programs/pygame_examples/cat.png')
# use relative path
cat = pygame.image.load("./pygame_examples/cat.png")
cat_x = 10
cat_y = 10
direction = 'right'
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if direction == 'right':
        cat_x += 5
        if cat_x == 720:
            direction = 'down'
    if direction == 'down':
        cat_y += 5
        if cat_y == 540:
            direction = 'left'
    if direction == 'left':
        cat_x -= 5
        if cat_x == 10:
            direction = 'up'
    if direction == 'up':
        cat_y -= 5
        if cat_y == 10:
            direction = 'right'
    screen.fill(WHITE)
    screen.blit(cat, (cat_x, cat_y))
    pygame.display.update()
    clock.tick(FPS)
