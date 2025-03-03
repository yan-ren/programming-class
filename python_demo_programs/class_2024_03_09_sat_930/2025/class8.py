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

player = Player(WIDTH // 2, HEIGHT // 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(30)
    screen.blit(player.image, player.rect)
    pygame.display.update()


pygame.quit()
