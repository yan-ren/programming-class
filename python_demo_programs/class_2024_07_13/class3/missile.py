import pygame.sprite

class Missile(pygame.sprite.Sprite):
    def __init__(self, window_height, x, y):
        super(Missile, self).__init__()
        self.window_height = window_height
        self.surf = pygame.Surface((10, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center = (x, y)
        )
        self.speed = 20

    def update(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.top < 0:
            self.kill()
