import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 1200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Move the Player')
font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

WEAPON_NAMES = {1: 'Normal', 2: 'Double', 3: 'Spread'}
MAX_WEAPON = 3

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.color = (0, 128, 255)
        self.speed = 5
        self.lives = 3
        self.weapon = 1
        self.max_weapon = 1

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
        elif self.y < 0:
            self.y = 0
        elif self.y > HEIGHT - self.size:
            self.y = HEIGHT - self.size

    def shoot(self):
        center_x = self.x + self.size // 2
        bullets = []

        if self.weapon == 1:
            bullets.append(Bullet(center_x, self.y))
        elif self.weapon == 2:
            bullets.append(Bullet(center_x - 12, self.y))
            bullets.append(Bullet(center_x + 4, self.y))
        elif self.weapon == 3:
            bullets.append(Bullet(center_x, self.y, dx = 0))
            bullets.append(Bullet(center_x, self.y, dx = -3))
            bullets.append(Bullet(center_x, self.y, dx = 3))
        return bullets

    def pickup_weapon(self):
        if self.max_weapon < MAX_WEAPON:
            self.max_weapon += 1
            self.weapon = self.max_weapon

    def switch_weapon(self, n):
        if 1 <= n <= self.max_weapon:
            self.weapon = n

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())


class Bullet:
    def __init__(self, x, y, dx = 0):
        self.x = x
        self.y = y
        self.dx = dx
        self.width = 8
        self.height = 20
        self.color = (255, 255, 0)
        self.speed = 10

    def move(self):
        self.y -= self.speed
        self.x += self.dx

    def is_off_screen(self):
        return self.y < 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

player = Player(200, 150)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill((30, 30, 30))
    player.draw(screen)
    pygame.display.update()
    clock.tick(60)