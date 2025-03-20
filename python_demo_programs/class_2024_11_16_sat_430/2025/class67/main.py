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

    def on_update(self, delta_time: float = 1/60):
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0

class RPSGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.LIGHT_GRAY)
        self.game_state = GameState.NOT_STARTED
        self.player_choice = None
        self.computer_choice = None
        self.result = "Press SPACE to start!"
        self.player_score = 0
        self.computer_score = 0

    def on_draw(self):
        self.clear()
        arcade.draw_text('Rock Paper Scissors', SCREEN_WIDTH//2,
                         SCREEN_HEIGHT // 2, arcade.color.BLACK, 18, anchor_x='center')
        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text(self.result, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.BLACK, 18,
                             anchor_x='center')
        else:
            for i, choice in enumerate(CHOICES):
                x = 100 + i * 200
                arcade.draw_lrbt_rectangle_filled(x, x + 120, 50, 150, arcade.color.WHITE)
                arcade.draw_text(choice, x, 150, arcade.color.BLACK, 16, anchor_x = 'center',
                                 anchor_y='center')
            arcade.draw_text(f'You: {self.player_choice}', SCREEN_WIDTH // 2, 220, arcade.color.BLUE,
                             16, anchor_x='center')
            arcade.draw_text(f'Computer: {self.computer_choice}', SCREEN_WIDTH // 2, 190,
                             arcade.color.RED, 16, anchor_x='center')
            arcade.draw_text(f'Score: {self.player_score} - {self.computer_score} Computer', SCREEN_WIDTH // 2,
                             50, arcade.color.BLACK, 16, anchor_x='center')
            arcade.draw_text(self.result, SCREEN_WIDTH // 2, 100, arcade.color.BLACK, 18, anchor_x = 'center')

    def on_mouse_press(self, x, y, button, modifiers):
        if self.game_state == GameState.ROUND_ACTIVE:
            for i, choice in enumerate(CHOICES):
                button_x = 100 + i * 200
                if button_x - 60 < x < button_x + 60 and 125 < y < 175:
                    self.play_game(choice)
                    break

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.game_state in [GameState.NOT_STARTED, GameState.ROUND_DONE]:
            self.result = "Choose Rock, Paper, or Scissors!"
            self.game_state = GameState.ROUND_ACTIVE
            self.player_choice = None
            self.computer_choice = None
        elif key == arcade.key.ENTER and self.game_state == GameState.GAME_OVER:
            self.player_score = 0
            self.computer_score = 0
            self.game_state = GameState.NOT_STARTED
            self.result = "Press SPACE to start!"

    def play_game(self, player_choice):
        self.player_choice = player_choice
        self.computer_choice = random.choice(CHOICES)

        if self.player_choice == self.computer_choice:
            self.result = "It's a tie!"
        elif (self.player_choice == "Rock" and self.computer_choice == "Scissors") or \
                (self.player_choice == "Paper" and self.computer_choice == "Rock") or \
                (self.player_choice == "Scissors" and self.computer_choice == "Paper"):
            self.result = "You win this round!"
            self.player_score += 1
        else:
            self.result = "You lose this round!"
            self.computer_score += 1

        if self.player_score == 3:
            self.result = "Congratulations! You won the game! Press ENTER to restart."
            self.game_state = GameState.GAME_OVER
        elif self.computer_score == 3:
            self.result = "Game over! Computer wins! Press ENTER to restart."
            self.game_state = GameState.GAME_OVER
        else:
            self.game_state = GameState.ROUND_DONE

game = RPSGame()
arcade.run()
