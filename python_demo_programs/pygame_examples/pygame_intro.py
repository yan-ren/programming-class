import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
FPS = 60
clock = pygame.time.Clock()
done = False

# RGB = R - Red, G - Green, B - Blue
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

cat_img = pygame.image.load('cat2.png')
cat_x = 10
cat_y = 10
direction = 'right'

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if direction == 'right':
        cat_x += 5
        if cat_x == 720:
            direction = 'down'
    elif direction == 'down':
        cat_y += 5
        if cat_y == 520:
            direction = 'left'
    elif direction == 'left':
        cat_x -= 5
        if cat_x == 10:
            direction = 'up'
    elif direction == 'up':
        cat_y -= 5
        if cat_y == 10:
            direction = 'right'

    screen.fill(WHITE)
    screen.blit(cat_img, (cat_x, cat_y))
    # update the screen
    pygame.display.update()
    clock.tick(FPS)