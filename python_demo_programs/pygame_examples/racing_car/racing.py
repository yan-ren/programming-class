import time
import pygame, sys, random

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
car = pygame.image.load('/Users/yan.ren/github.com/yan.ren/programming-class/python_demo_programs/pygame_examples/racing_car/car1.png')
FPS = 60


def crash():
    message_display("You crashed!", 115, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    time.sleep(3)


def message_display(msg, font_size, x_pos, y_pos):
    text_style = pygame.font.Font('freesansbold.ttf', font_size)
    text_surf = text_style.render(msg, True, BLACK)
    text_rect = text_surf.get_rect()
    text_rect.center = (x_pos, y_pos)
    display.blit(text_surf, text_rect)
    pygame.display.update()


def draw_block(x, y, width, height, color):
    pygame.draw.rect(display, color, (x, y, width, height))


def place_car(x, y):
    display.blit(car, (x, y))


def game_loop():
    car_x = WINDOW_WIDTH * 0.45
    car_y = WINDOW_HEIGHT * 0.9
    car_x_change = 0
    block_x = random.randint(0, WINDOW_WIDTH)
    block_y = 0
    block_speed = 7
    block_width = 100
    block_height = 100
    block_passed = False
    score = 0

    crashed = False
    global FPS

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -5
                elif event.key == pygame.K_RIGHT:
                    car_x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    car_x_change = 0

        if car_x < 0:
            car_x = 0
        elif car_x > WINDOW_WIDTH - car.get_width():
            car_x = WINDOW_WIDTH - car.get_width()
        else:
            car_x += car_x_change

        # collision
        if block_y + block_height > car_y:
            if block_x < car_x < block_x + block_width or block_x < car_x + car.get_width() < block_x + block_width:
                crash()
                return
            elif not block_passed:
                score += 1
                block_passed = True

        block_y += block_speed
        if block_y > WINDOW_HEIGHT:
            block_y = -block_height
            block_x = random.randint(0, WINDOW_WIDTH)

        display.fill(WHITE)
        place_car(car_x, car_y)
        draw_block(block_x, block_y, block_width, block_height, BLACK)
        pygame.display.update()
        clock.tick(FPS)


def frame_countdown():
    countdown_text = ['3', '2', '1', 'Game Start!']
    text_index = 0
    current_text = countdown_text[text_index]
    start_tick = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # only change text after running several frame
        current_tick = pygame.time.get_ticks()
        if (current_tick - start_tick) / 1000 > 1:
            text_index += 1
            if text_index == len(countdown_text):
                break
            current_text = countdown_text[text_index]
            start_tick = current_tick

        # screen display
        display.fill(WHITE)
        message_display(current_text, 100, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

        # FPS
        clock.tick(FPS)


if __name__ == "__main__":
    frame_countdown()
    game_loop()
    pygame.quit()
    sys.exit()
