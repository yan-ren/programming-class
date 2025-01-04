import pygame
import random
import time

pygame.init()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
car = pygame.image.load('C:\\Users\\github.com\\programming-class\\python_demo_programs\\pygame_examples\\racing_car\\car1.png')
clock = pygame.time.Clock()


def crash():
    msg_display("You crashed!", 120, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    time.sleep(3)
    exit()


def msg_display(msg, font_size, x_pos, y_pos):
    text_style = pygame.font.Font('freesansbold.ttf', font_size)
    text_surf = text_style.render(msg, True, BLACK)
    text_rect = text_surf.get_rect()
    text_rect.center = (x_pos, y_pos)
    screen.blit(text_surf, text_rect)
    pygame.display.update()


def draw_block(x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))


def count_down_frame():
    countdown_text = ['3', '2', '1', 'Game Start!']
    text_index = 0
    current_text = countdown_text[text_index]
    start_tick = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # only change text after running several frame
        current_tick = pygame.time.get_ticks()
        if current_tick - start_tick > 1000:
            text_index += 1
            # all text displayed
            if text_index == len(countdown_text):
                return

            current_text = countdown_text[text_index]
            start_tick = pygame.time.get_ticks()

        screen.fill(WHITE)
        msg_display(current_text, 100, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)


def game_loop():
    car_x = WINDOW_WIDTH / 2
    car_y = WINDOW_HEIGHT - car.get_height()
    car_x_change = 0
    # block type A
    block_x = random.randint(0, WINDOW_WIDTH)
    block_y = 0
    block_width = 100
    block_height = 100
    block_speed = 7
    # block type B
    block_b_x = random.randint(0, WINDOW_WIDTH)
    block_b_y = 0
    block_b_width = block_b_height = 50
    block_b_speed = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -5
                elif event.key == pygame.K_RIGHT:
                    car_x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    car_x_change = 0

        # stop car from move outside of the screen
        if car_x < 0:
            car_x = 0
        elif car_x > WINDOW_WIDTH - car.get_width():
            car_x = WINDOW_WIDTH - car.get_width()
        else:
            car_x += car_x_change

        # change y of the block
        block_y += block_speed
        if block_y > WINDOW_HEIGHT:
            block_y = -block_height
            block_x = random.randint(0, WINDOW_WIDTH)

        block_b_y += block_b_speed
        if block_b_y > WINDOW_HEIGHT:
            block_b_y = -block_b_height
            block_b_x = random.randint(0, WINDOW_WIDTH)

        # collision detection
        if car_y < block_y + block_height:
            if block_x < car_x < block_x + block_width or block_x < car_x + car.get_width() < block_x + block_width:
                crash()

        screen.fill(WHITE)
        screen.blit(car, (car_x, car_y))
        draw_block(block_x, block_y, block_width, block_height, BLACK)
        draw_block(block_b_x, block_b_y, block_b_width, block_b_height, BLUE)
        pygame.display.update()


if __name__ == "__main__":
    count_down_frame()
    game_loop()


'''
create a score on the top right corner of the screen
everytime by pass a block, user score by 1
hint: use msg_display to write score on screen
'''