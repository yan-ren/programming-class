import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    pygame.display.update()
