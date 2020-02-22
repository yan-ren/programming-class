import pygame
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

# r g b
yellow = (255, 255, 0)
black = (0, 0, 0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.circle(screen, yellow, (600, 200), 50)
    pygame.draw.circle(screen, black, (575, 180), 7)
    pygame.draw.circle(screen, black, (625, 180), 7)
    smile_rect = pygame.Rect(575, 210, 50, 20)
    pygame.draw.arc(screen, black, smile_rect, math.pi, 2 * math.pi, 3)
    pygame.display.update()
