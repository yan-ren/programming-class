import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

# RGB = R - Red, G - Green, B - Blue
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    #                              x,   y,  width, height
    pygame.draw.rect(screen, RED, [40, 200, 100, 70], 1)
    pygame.draw.rect(screen, GREEN, [200, 200, 100, 100], 0)
    pygame.draw.line(screen, BLACK, [0, 0], [400, 300], 5)

    # update the screen
    pygame.display.update()