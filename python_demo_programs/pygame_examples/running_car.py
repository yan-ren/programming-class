import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
# rgb
WHITE = (255, 255, 255)
car = pygame.image.load('racing_car/red_car.png')
clock = pygame.time.Clock()
x = 0
y = 0
direction = 'right'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if direction == 'right':
        x += 5
        if x > 720:
            direction = 'down'
    if direction == 'down':
        y += 5
        if y > 520:
            direction = 'left'
    if direction == 'left':
        x -= 5
        if x <= 0:
            direction = 'up'
    if direction == 'up':
        y -= 5
        if y <= 0:
            direction = 'right'

    car.get_width()
    car.get_height()
    screen.fill(WHITE)
    screen.blit(car, (x, y))
    pygame.display.update()
    clock.tick(60)














'''
given two list, list1 and list2, list1 is sorted, list2 is unsorted,
insert each element in list2 into list1 and keep sorted order, don't use list.sort() method

list1 = [1, 4, 5, 6]
list2 = [3, 2]

[1, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
'''