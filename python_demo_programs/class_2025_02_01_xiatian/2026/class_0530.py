import pygame
import random
import sys


pygame.init()

WIDTH = 1200
HEIGHT = 1500

# Automatically launches in your monitor's native resolution
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

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

        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH - self.size:
            self.x = WIDTH - self.size
        if self.y > HEIGHT - self.size:
            self.y = HEIGHT - self.size
        elif self.y < 0:
            self.y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

'''
1. key.get_pressed
2. move based on key
3. blit on screen
'''
running = True
player = Player(200, 200)
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # complete
    player.move(keys)

    screen.fill((30, 30, 30))
    player.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()