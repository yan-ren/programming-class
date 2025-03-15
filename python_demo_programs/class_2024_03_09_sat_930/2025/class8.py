# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
#     # call instance method through specific object
#     def start(self):
#         print(self.brand, 'starts')
#
# # object = class
# car1 = Car('toyota', 2020)
# car2 = Car('honda', 2021)
#
# car1.start()
# car2.start()
import time
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.trail = []

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Add current position to trail
        self.trail.append((self.rect.x, self.rect.y, time.time()))

        # remove old trail position after 3 seconds
        self.trail =[(x, y, t) for x, y, t in self.trail if time.time() - t < 3]

player = Player(WIDTH // 2, HEIGHT // 2)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)
    pygame.time.delay(30)

    #
    screen.fill((0, 0, 0))

    # draw trail
    for x, y, _ in player.trail:
        pygame.draw.rect(screen, (0, 128, 255, 100), (x, y, 50, 50))
    # draw player
    screen.blit(player.image, player.rect)
    pygame.display.update()


pygame.quit()
