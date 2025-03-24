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
        self.current_texture_index = 0
        self.set_texture(self.current_texture_index)

        self.center_x = x
        self.center_y = y
        self.time_since_last_swap = 0.0
        self.animation_update_time = 1.0 / self.ANIMATION_SPEED

    def load_textures(self):
        """Load the correct textures for each attack type."""
        if self.attack_type == AttackType.ROCK:
            return [
                arcade.load_texture("assets/srock.png"),
                arcade.load_texture("assets/srock-attack.png"),
            ]
        elif self.attack_type == AttackType.PAPER:
            return [
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/spaper-attack.png"),
            ]
        else:  # AttackType.SCISSORS
            return [
                arcade.load_texture("assets/scissors.png"),
                arcade.load_texture("assets/scissors-close.png"),
            ]

    def update_animation(self, delta_time: float = 1 / 60):
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture_index = (self.current_texture_index + 1) % len(self.textures)
            self.set_texture(self.current_texture_index)
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

        # Initialize the sprite list
        self.attack_animations = arcade.SpriteList()

        # Load attack animations and add them to the sprite list
        self.rock = AttackAnimation(AttackType.ROCK, 100, 300)
        self.paper = AttackAnimation(AttackType.PAPER, 300, 300)
        self.scissors = AttackAnimation(AttackType.SCISSORS, 500, 300)

        self.attack_animations.append(self.rock)
        self.attack_animations.append(self.paper)
        self.attack_animations.append(self.scissors)

    def on_draw(self):
        """Render the game visuals."""
        self.clear()
        arcade.draw_text('Rock Paper Scissors', SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT - 50, arcade.color.BLACK, 18, anchor_x='center')

        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text(self.result, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.BLACK, 18,
                             anchor_x='center')
        else:
            # Display game state text
            arcade.draw_text(f'You: {self.player_choice}', SCREEN_WIDTH // 2, 220, arcade.color.BLUE,
                             16, anchor_x='center')
            arcade.draw_text(f'Computer: {self.computer_choice}', SCREEN_WIDTH // 2, 190,
                             arcade.color.RED, 16, anchor_x='center')
            arcade.draw_text(f'Score: {self.player_score} - {self.computer_score} Computer', SCREEN_WIDTH // 2,
                             50, arcade.color.BLACK, 16, anchor_x='center')
            arcade.draw_text(self.result, SCREEN_WIDTH // 2, 100, arcade.color.BLACK, 18, anchor_x='center')

            # Draw animations
            self.attack_animations.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """Detects player clicks to choose an attack based on texture."""
        if self.game_state == GameState.ROUND_ACTIVE:
            for animation in self.attack_animations:
                # Check if the click is within the sprite's bounds
                if animation.left < x < animation.right and animation.bottom < y < animation.top:
                    # Map the AttackType to the corresponding choice string
                    if animation.attack_type == AttackType.ROCK:
                        player_choice = "Rock"
                    elif animation.attack_type == AttackType.PAPER:
                        player_choice = "Paper"
                    elif animation.attack_type == AttackType.SCISSORS:
                        player_choice = "Scissors"

                    self.play_game(player_choice)
                    break


    def on_key_press(self, key, modifiers):
        """Handles keyboard inputs for game state changes."""
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
        """Determines round result and updates game state."""
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

    def on_update(self, delta_time):
        for animation in self.attack_animations:
            animation.update_animation(delta_time)


game = RPSGame()
arcade.run()
