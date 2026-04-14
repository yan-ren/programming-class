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

        if self.x > WIDTH - self.size:
            self.x = WIDTH - self.size
        if self.x < 0:
            self.x = 0

        if self.y > HEIGHT - self.size:
            self.y = HEIGHT - self.size
        if self.y < 0:
            self.y = 0

    def shoot(self):
        bullet_x = self.x + self.size // 2
        bullet_y = self.y
        return Bullet(bullet_x, bullet_y)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 20
        self.color = (255, 255, 0)
        self.speed = 10

    def move(self):
        self.y -= self.speed

    def is_off_screen(self):
        return self.y < 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class Enemy:
    def __init__(self):
        self.size = 50
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(-200, -self.size)
        self.color = (220, 50, 50)
        self.speed = random.randint(2, 5)

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > HEIGHT

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


player = Player(200, 150)
enemies = [Enemy() for _ in range(5)]
bullets = []
shoot_cooldown = 0
running = True
new_enemy_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    if shoot_cooldown > 0:
        shoot_cooldown -= 1

    if keys[pygame.K_SPACE] and shoot_cooldown == 0:
        bullets.append(player.shoot())
        shoot_cooldown = 5

    for bullet in bullets:
        bullet.move()

    for enemy in enemies:
        enemy.move()

    enemies = [e for e in enemies if not e.is_off_screen()]
    new_enemy_timer += 1
    if new_enemy_timer >= 90:
        enemies.append(Enemy())
        new_enemy_timer = 0

    bullets = [b for b in bullets if not b.is_off_screen()]

    screen.fill((30, 30, 30))
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()