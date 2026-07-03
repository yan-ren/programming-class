import pygame
import random
import sys


pygame.init()

WIDTH = 1200
HEIGHT = 1500

# Automatically launches in your monitor's native resolution
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 48)

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

    def shoot(self):
        bullet_x = self.x + self.size // 2
        bullet_y = self.y

        return Bullet(bullet_x, bullet_y)


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

class Enemy:
    def __init__(self):
        self.size = 50
        self.speed = random.randint(2, 5)
        self.color = (220, 50, 50)
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(-200, -self.size)

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > HEIGHT

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

class Coin:
    def __init__(self):
        self.size = 30
        self.speed = 3
        self.color = (255, 215, 0)  # gold
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(-200, -self.size)

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > HEIGHT

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        center_x = self.x + self.size // 2
        center_y = self.y + self.size // 2
        radius = self.size // 2
        pygame.draw.circle(screen, self.color, (center_x, center_y), radius)
        
'''
1. key.get_pressed
2. move based on key
3. blit on screen
'''
running = True
player = Player(200, 200)
clock = pygame.time.Clock()
bullets = []
enemies = []
shoot_cooldown = 15
spawn_enemy = 0
score = 0
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if shoot_cooldown > 0:
        shoot_cooldown -= 1

    spawn_enemy += 1
    if spawn_enemy >= 90:
        enemies.append(Enemy())
        spawn_enemy = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shoot_cooldown == 0:
        bullet = player.shoot()
        shoot_cooldown = 15
        bullets.append(bullet)

    # complete
    player.move(keys)
    for bullet in bullets:
        bullet.move()
    bullets = [b for b in bullets if not b.is_off_screen()]

    for enemy in enemies:
        enemy.move()
    enemies = [e for e in enemies if not e.is_off_screen()]

    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.get_rect().colliderect(enemy.get_rect()):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    for enemy in enemies[:]:
        if player.get_rect().colliderect(enemy.get_rect()):
            enemies.remove(enemy)
            player.lives -= 1
            if player.lives <= 0:
                running = False

    elapsed_seconds = (pygame.time.get_ticks() - start_time) / 1000

    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    lives_text = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
    timer_text = font.render(f'Time: {elapsed_seconds}', True, (255, 255, 255))

    screen.fill((30, 30, 30))
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 60))
    screen.blit(timer_text, (WIDTH - timer_text.get_width() - 10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()