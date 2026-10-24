import pygame

def calculate(first, second, operator):
    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "/":
        if second == 0:
            return "Error"
        return first / second

def main():
    pygame.init()
    screen = pygame.display.set_mode((360, 490))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

    background = (25, 30, 42)
    number_color = (61, 71, 90)
    operator_color = (45, 111, 180)
    clear_color = (165, 65, 75)
    white = (245, 247, 250)

    layout = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
    ]