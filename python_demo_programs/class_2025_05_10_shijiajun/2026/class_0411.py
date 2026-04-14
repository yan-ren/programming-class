# python class -> object oriented programming
# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#
#     def bark(self):
#         print('Woof! Woof!')

# dog1 = Dog('Buddy', 'Golden', 3)
# print(dog1.name)
# print(dog1.age)
#
# dog2 = Dog("Luna", "Husky", 5)
# print(dog2.breed)
#
# dog1.name = 'Bob'
# dog1.bark()
# dog2.bark()

# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.energy = 100
#
#     def fetch(self, item):
#         self.energy -= 10
#         print(f'{self.name} fetches the {item}! Energy: {self.energy}')
#
#     def nap(self):
#         self.energy += 30
#
#
# buddy = Dog("Buddy")
# buddy.fetch("ball")
# buddy.fetch("stick")
# buddy.nap()

import pygame

class Player:
    def __init__(self, x, y, color, speed):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = color
        self.speed = speed
        self.score = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed