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

class Enemy:
    def __init__(self):
        self.size = 40
        self.speed = random.randint(2, 5)
        self.color = (220, 50, 50)
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(-200, -self.size)

    def move(self, player):
        self.y += self.speed
        if player.x > self.x:
            self.x += 1
        elif player.x < self.x:
            self.x -= 1

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
        self.color = (255, 215, 0)
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


class Weapon:
    def __init__(self):
        self.size = 35
        self.speed = 3
        self.color = (0, 255, 255)
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(-200, -self.size)

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > HEIGHT

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        points = [
            (self.x + self.size // 2, self.y),
            (self.x, self.y + self.size),
            (self.x + self.size, self.y + self.size)
        ]
        pygame.draw.polygon(screen, self.color, points)

player = Player(200, 150)
bullets = []
enemies= [Enemy() for _ in range(5)]
weapon_pickup = []
coins = []
shoot_cooldown = 15
spawn_timer = 0
weapon_spawn_timer = 0
coin_spawn_timer = 0
running = True

score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    # switch weapon with number keys
    if keys[pygame.K_1]:
        player.switch_weapon(1)
    if keys[pygame.K_2]:
        player.switch_weapon(2)
    if keys[pygame.K_3]:
        player.switch_weapon(3)

    if shoot_cooldown > 0:
        shoot_cooldown -= 1

    spawn_timer += 1
    if spawn_timer >= 90:
        enemies.append(Enemy())
        spawn_timer = 0

    coin_spawn_timer += 1
    if coin_spawn_timer >= 180:
        coins.append(Coin())
        coin_spawn_timer = 0

    weapon_spawn_timer += 1
    if weapon_spawn_timer >= 360:
        weapon_pickup.append(Weapon())
        weapon_spawn_timer = 0

    if keys[pygame.K_SPACE] and shoot_cooldown == 0:
        new_bullets = player.shoot()
        bullets.extend(new_bullets)
        shoot_cooldown = 15

    for bullet in bullets:
        bullet.move()
    bullets = [b for b in bullets if not b.is_off_screen()]

    for enemy in enemies:
        enemy.move(player)
    enemies = [e for e in enemies if not e.is_off_screen()]

    for coin in coins:
        coin.move()
        coins = [c for c in coins if not c.is_off_screen()]

    for wp in weapon_pickup:
        wp.move()
        weapon_pickup = [w for w in weapon_pickup if not w.is_off_screen()]

    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.get_rect().colliderect(enemy.get_rect()):
                bullets.remove(bullet)
                enemies.remove(enemy)

    for enemy in enemies[:]:
        if player.get_rect().colliderect(enemy.get_rect()):
            enemies.remove(enemy)
            player.lives -= 1
            if player.lives <= 0:
                running = False

    for coin in coins[:]:
        if player.get_rect().colliderect(coin.get_rect()):
            coins.remove(coin)
            player.lives += 1

    for wp in weapon_pickup[:]:
        if player.get_rect().colliderect(wp.get_rect()):
            weapon_pickup.remove(wp)
            player.pickup_weapon()

    screen.fill((30, 30, 30))
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for coin in coins:
        coin.draw(screen)
    for wp in weapon_pickup:
        wp.draw(screen)

    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    lives_text = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
    # timer_text = font.render(f'Time: {elapsed_seconds}', True, (255, 255, 255))
    weapon_label = f'Weapon: {WEAPON_NAMES[player.weapon]} ({player.weapon} / {player.max_weapon})'
    weapon_text = font.render(weapon_label, True, (0, 255, 255))

    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 60))
    # screen.blit(timer_text, (WIDTH - timer_text.get_width() - 10, 10))
    screen.blit(weapon_text, (10, 110))

    pygame.display.update()
    clock.tick(60)