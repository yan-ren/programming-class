import pygame
import random
import sys

pygame.init()

# constant
WIDTH = 1200
HEIGHT = 1200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.color = (0, 128, 255)
        self.speed = 5
        self.lives = 3

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def shoot(self):
        center_x = self.x + self.size // 2
        bullets = []

        bullets.append(Bullet(center_x, self.y))
        return bullets

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


player= Player(200, 150)
bullets = []
shoot_cooldown = 15

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    if shoot_cooldown > 0:
        shoot_cooldown -= 1

    if keys[pygame.K_SPACE] and shoot_cooldown == 0:
        new_bullets = player.shoot()
        bullets.extend(new_bullets)
        shoot_cooldown = 15

    for bullet in bullets:
        bullet.move()
    bullets = [b for b in bullets if not b.is_off_screen()]

    # draw
    screen.fill((30, 30, 30))
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.update()
    clock.tick(60)