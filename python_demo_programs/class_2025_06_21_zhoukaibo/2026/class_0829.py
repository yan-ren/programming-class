import pygame
import random
import sys

pygame.init()

# constant
WIDTH = 1200
HEIGHT = 1200
MAX_WEAPON = 3

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
        if self.y > HEIGHT - self.size:
            self.y = HEIGHT - self.size
        elif self.y < 0:
            self.y = 0

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


class Enemy:
    def __init__(self):
        self.size = 50
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


player= Player(200, 150)
enemies = [Enemy() for _ in range(5)]
bullets = []
coins = []
coin_spawn_timer = 0
shoot_cooldown = 15
spawn_timer = 0
score = 0

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

    for enemy in enemies:
        enemy.move(player)
    enemies = [e for e in enemies if not e.is_off_screen()]

    spawn_timer += 1
    if spawn_timer >= 90:
        enemies.append(Enemy())
        spawn_timer = 0

    for coin in coins:
        coin.move()
    coins = [c for c in coins if not c.is_off_screen()]

    coin_spawn_timer += 1
    if coin_spawn_timer >= 180:
        coins.append(Coin())
        coin_spawn_timer = 0

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

    # draw
    screen.fill((30, 30, 30))
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for coin in coins:
        coin.draw(screen)

    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    lives_text = font.render(f'Lives: {player.lives}', True, (255, 255, 255))

    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 60))

    pygame.display.update()
    clock.tick(60)

screen.fill((30, 30, 30))
game_over_text = font.render(f'Game Over!', True, (255, 255, 255))
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height()))
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()
sys.exit()