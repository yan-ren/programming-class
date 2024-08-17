import pygame.sprite

class Plane(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height):
        super(Plane, self).__init__()
        self.surf = pygame.Surface((25, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect = self.surf.get_rect(
            center = (window_width / 2, window_height / 2)
        )
        self.window_width = window_width
        self.window_height = window_height

    def update(self, pressed_key):
        if pressed_key[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_key[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_key[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_key[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # keep plane on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.window_width:
            self.rect.right = self.window_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.window_height:
            self.rect.bottom = self.window_height
