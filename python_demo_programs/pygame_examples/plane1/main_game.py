import pygame

from pygame_examples.plane1.plane import Plane

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
plane = Plane()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    screen.blit(plane.surf, plane.rect)
    plane.update(pygame.key.get_pressed())
    pygame.display.update()
    clock.tick(FPS)
