# Define a Plane class by extending pgyame.sprite.Sprite class
import pygame.sprite


class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super(Plane, self).__init__()
        # surf is a white rectangular represents the plane
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        # rect is used to define the position of the surf
        self.rect = self.surf.get_rect()

    # Move the sprite based on user key press
    def update(self, pressed_key):
        if pressed_key[pygame.K_UP]:
            self.rect.move_ip(0, -5)