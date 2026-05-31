import random
import pygame
import sys


pygame.init()

WIDTH = 1200
HEIGHT = 1200

WEAPON_NAMES = {1: 'Normal', 2: 'Double', 3: 'Spread'}
MAX_WEAPON = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Player")
font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

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

        if self.x > WIDTH - self.size:
            self.x = WIDTH - self.size
        if self.x < 0:
            self.x = 0

        if self.y > HEIGHT - self.size:
            self.y = HEIGHT - self.size
        if self.y < 0:
            self.y = 0

    def shoot(self):
        center_x = self.x + self.size // 2
        bullets = []
        if self.weapon == 1:
            bullets.append(Bullet(center_x, self.y))
        elif self.weapon == 2:
            bullets.append(Bullet(center_x - 12, self.y))
            bullets.append(Bullet(center_x + 4, self.y))
        elif self.weapon == 3:
            bullets.append(Bullet(center_x, self.y, dx=0))
            bullets.append(Bullet(center_x, self.y, dx=-3))
            bullets.append(Bullet(center_x, self.y, dx=3))
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
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


class Bullet:
    def __init__(self, x, y, dx=0, dy=-10, color=(255, 255, 0), damage=1, width=8):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = 20
        self.color = color
        self.damage = damage

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def is_off_screen(self):
        return self.y < 0 or self.x < -self.width or self.x > WIDTH

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class Enemy:
    def __init__(self):
        self.size = 50
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(-200, -self.size)
        self.speed = random.randint(2, 5)
        self.horizontal_speed = random.randint(1, 5)
        self.lives = random.choice([1, 2, 3])
        if self.lives == 1:
            self.color = (220, 50, 50)
        elif self.lives == 2:
            self.color = (150, 0, 150)
        else:
            self.color = (220, 50, 50)


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

    def hit(self):
        self.lives -= 1
        if self.lives == 1:
            self.color = (220, 50, 50)

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
weapon_pickups = []
new_coin_timer = 0
weapon_spawn_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    # switch weapon with number keys (only if unlocked)
    if keys[pygame.K_1]:
        player.switch_weapon(1)
    if keys[pygame.K_2]:
        player.switch_weapon(2)
    if keys[pygame.K_3]:
        player.switch_weapon(3)

    if shoot_cooldown > 0:
        shoot_cooldown -= 1

    if keys[pygame.K_SPACE] and shoot_cooldown == 0:
        new_bullets = player.shoot()
        bullets.extend(new_bullets)
        shoot_cooldown = 15

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

    for wp in weapon_pickups:
        wp.move()
    weapon_pickups = [w for w in weapon_pickups if not w.is_off_screen()]

    weapon_spawn_timer += 1
    if weapon_spawn_timer >= 360:  # rarer than coins
        weapon_pickups.append(Weapon())
        weapon_spawn_timer = 0

    for wp in weapon_pickups[:]:
        if player.get_rect().colliderect(wp.get_rect()):
            weapon_pickups.remove(wp)
            player.pickup_weapon()

    # bullet vs enemy collision
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.get_rect().colliderect(enemy.get_rect()):
                bullets.remove(bullet)
                enemy.hit()
                if enemy.lives <= 0:
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
    weapon_label = f'Weapon: {WEAPON_NAMES[player.weapon]} ({player.weapon} / {player.max_weapon})'
    weapon_text = font.render(weapon_label, True, (0, 255, 255))

    # drawing
    screen.fill((30, 30, 30))
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for coin in coins:
        coin.draw(screen)
    for wp in weapon_pickups:
        wp.draw(screen)

    screen.blit(timer_text, (10, 10))
    screen.blit(score_text, (10, 50))
    screen.blit(lives_text, (10, 90))
    screen.blit(weapon_text, (10, 110))

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
5. add coin object, when player gets it, lives + 1
6. different type of enemy, some enemy can have more lives, e.g. need to be shoot by 2 bullet to disappear

today:
1. different type of weapons, create special coin representing weapon, when player gets it, player have a new weapon,
and can use key to switch between the weapon, different weapon can be shown on the screen

- Weapon class
- Player class adds two attributes, and two method (pickup_weapon(), switch_weapon(n))
- Player.shoot()
- Bullet uses dx, updates is_off_screen
'''