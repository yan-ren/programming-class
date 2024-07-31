import random

import pygame.sprite
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((10, 20)) # create a rectangle
        self.surf.fill((255, 255, 255))
        # setup surf initial position
        self.rect = self.surf.get_rect(
            center = (random.randint(0, window_width), random.randint(-100, -20))
        )
        self.window_height = window_height

    def update(self):
        self.rect.move_ip(0, random.randint(5, 10))
        if self.rect.top > self.window_height:
            self.kill()

