import random
import pygame
import sys

pygame.init()

WIDTH = 1200
HEIGHT = 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Player")

clock = pygame.time.Clock()
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
        self.horizontal_speed = random.randint(1, 5)

    def move(self, player_x):
        self.y += self.speed
        if self.x < player_x:
            self.x += self.horizontal_speed
        elif self.x > player_x:
            self.x -= self.horizontal_speed

    def is_off_screen(self):
        return self.y > HEIGHT

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


class Coin:
    def __init__(self):
        self.size = 30
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(-200, -self.size)
        self.color = (255, 215, 0)
        self.speed = 3

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > HEIGHT

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        center = (self.x + self.size // 2, self.y + self.size // 2)
        pygame.draw.circle(screen, self.color, center, self.size // 2)


player = Player(200, 150)
enemies = [Enemy() for _ in range(5)]
bullets = []
shoot_cooldown = 0
running = True
new_enemy_timer = 0
score = 0
start_time = pygame.time.get_ticks()
coins = []
new_coin_timer = 0

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
        enemy.move(player.x)

    for coin in coins:
        coin.move()

    enemies = [e for e in enemies if not e.is_off_screen()]
    bullets = [b for b in bullets if not b.is_off_screen()]
    coins = [c for c in coins if not c.is_off_screen()]

    new_coin_timer += 1
    if new_coin_timer >= 300:   # spawn one every ~5 seconds
        coins.append(Coin())
        new_coin_timer = 0

    new_enemy_timer += 1
    if new_enemy_timer >= 90:
        enemies.append(Enemy())
        new_enemy_timer = 0

    # player vs coin collision
    for coin in coins[:]:
        if player.get_rect().colliderect(coin.get_rect()):
            coins.remove(coin)
            player.lives += 1

    # bullet vs enemy collision
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.get_rect().colliderect(enemy.get_rect()):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # player vs enemy collision
    for enemy in enemies[:]:
        if player.get_rect().colliderect(enemy.get_rect()):
            enemies.remove(enemy)
            player.lives -= 1
            if player.lives <= 0:
                running = False

    elapsed_seconds = (pygame.time.get_ticks() - start_time) / 1000
    timer_text = font.render(f'Time: {elapsed_seconds}', True, (255, 255, 255))
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    lives_text = font.render(f'Lives: {player.lives}', True, (255, 255, 255))

    # drawing
    screen.fill((30, 30, 30))
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for coin in coins:
        coin.draw(screen)
    screen.blit(timer_text, (10, 10))
    screen.blit(score_text, (10, 50))
    screen.blit(lives_text, (10, 90))

    pygame.display.update()
    clock.tick(60)

screen.fill((30, 30, 30))

game_over_text = font.render(f'Game Over!', True, (255, 255, 255))
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()
sys.exit()

'''
done
1. bullet can destroy the enemy
2. player has lives, when collide with enemy, lives are reduced by one
3. add timer that starts from zero, show timer on the screen
4. showing score and lives on the screen

today:
1. add coin object, when player gets it, lives + 1

'''