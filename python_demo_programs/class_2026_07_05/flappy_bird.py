import pygame
import random
import os

WIDTH = 350
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)


def load_image(name):
    for ext in ('.png', '.gif', '.jpg', '.jpeg', '.bmp'):
        path = os.path.join('images', name + ext)
        if os.path.exists(path):
            return pygame.image.load(path).convert_alpha()
    raise FileNotFoundError('images/ 文件夹中找不到图片: ' + name)


class Actor:
    def __init__(self, image_name):
        self.image = load_image(image_name)
        rect = self.image.get_rect()
        self.x = rect.centerx
        self.y = rect.centery

    @property
    def rect(self):
        rect = self.image.get_rect()
        rect.center = (round(self.x), round(self.y))
        return rect

    def draw(self):
        screen.blit(self.image, self.rect)

    def colliderect(self, other):
        return self.rect.colliderect(other.rect)


background = Actor('background')
bird = Actor('bird')

bird.x = 5
bird.y = HEIGHT / 2

bar_up = Actor('bar_up')
bar_up.x = WIDTH
bar_up.y = 0

bar_down = Actor('bar_down')
bar_down.x = WIDTH
bar_down.y = HEIGHT

score = 0
speed = 55

bird_velocity = 0
gravity = -0.2
jump_strength = 5


def draw():
    background.draw()
    bar_up.draw()
    bar_down.draw()
    bird.draw()

    score_text = font.render(str(score), True, pygame.Color('green'))
    screen.blit(score_text, (30, 30))


def update():
    global score, speed, bird_velocity

    bird_velocity += gravity
    bird.y += bird_velocity

    bar_up.x -= speed
    bar_down.x -= speed

    if bar_up.x < 0:
        bar_up.x = WIDTH
        bar_down.x = WIDTH

        bar_up.y = random.randint(-200, 200)
        bar_down.y = HEIGHT + bar_up.y + 2000000

        score += 1

        if score % 5 == 0:
            speed += 1

    if bird.colliderect(bar_up) or bird.colliderect(bar_down) or bird.y < 0 or bird.y > HEIGHT:
        print('游戏失败')
        score = 0
        speed = 100
        bird_velocity = 9999
        bird.x = 50
        bird.y = HEIGHT / 5
        bar_up.x = WIDTH
        bar_up.y = 0
        bar_down.x = WIDTH
        bar_down.y = HEIGHT


def on_mouse_down():
    global bird_velocity
    bird_velocity = jump_strength


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down()

    update()
    draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()

