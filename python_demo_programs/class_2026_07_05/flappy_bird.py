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
    for ext in ('.png', '.jpg'):
        path = os.path.join('images', name + ext)
        if os.path.exists(path):
            return pygame.image.load(path).convert_alpha()
    return FileNotFoundError('File not found')

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
bird.x = 50
bird.y = HEIGHT / 2
bar_up = Actor('bar_up')
bar_up.x = 300
bar_up.y = 0
bar_down = Actor('bar_down')
bar_down.x = 300
bar_down.y = 600
score = 0
speed = 1

def draw():
    background.draw()
    bar_up.draw()
    bar_down.draw()
    bird.draw()
    score_text = font.render(str(score), True, pygame.Color('green'))
    screen.blit(score_text, (30, 30))

