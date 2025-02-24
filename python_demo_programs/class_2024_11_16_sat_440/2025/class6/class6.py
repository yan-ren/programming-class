import arcade
import random
from enum import Enum

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
TITLE = 'Rock Paper Scissors'
CHOICES = ['Rock', 'Paper', 'Scissors']


class GameState(Enum):
    NOT_STARTED = 0
    ROUND_ACTIVE = 1
    ROUND_DONE = 2
    GAME_OVER = 3


class AttackType(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class AttackAnimation(arcade.Sprite):
    ATTACK_SCALE = 0.5
    ANIMATION_SPEED = 5.0

    def __init__(self, attack_type, x, y):
        super().__init__()
        self.attack_type = attack_type
        self.textures = self.load_textures()

        self.scale = self.ATTACK_SCALE
        self.current_texture = 0
        self.set_texture(self.current_texture)

        self.center_x = x
        self.center_y = y
        self.time_since_last_swap = 0.0
        self.animation_update_time = 1.0 / self.ANIMATION_SPEED

    def load_textures(self):
        if self.attack_type == AttackType.ROCK:
            self.textures = [
                arcade.load_texture("assets/srock.png"),
                arcade.load_texture("assets/srock-attack.png"),
            ]
        elif self.attack_type == AttackType.PAPER:
            self.textures = [
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/spaper-attack.png"),
            ]
        else:
            self.textures = [
                arcade.load_texture("assets/scissors.png"),
                arcade.load_texture("assets/scissors-close.png"),
            ]