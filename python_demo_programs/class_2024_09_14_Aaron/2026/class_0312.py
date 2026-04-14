import random

import pygame
import sys

pygame.init()

WIDTH = 1200
HEIGHT = 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Player")

clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.color = (0, 128, 255)
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def change_color(self, keys):
        if keys[pygame.K_SPACE]:
            self.color = random.choice([(245, 123, 66), (90, 245, 66), (66, 114, 245)])

player = Player(200, 150)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.move(keys)
    player.change_color(keys)

    screen.fill((30, 30, 30))
    player.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()