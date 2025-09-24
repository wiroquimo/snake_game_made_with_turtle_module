"""
game.py

Encapsulates full Snake game logic, using event-driven movement
and asynchronous blinking without time.sleep().
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


class Game:
    """Main Snake game class (fully asynchronous)."""

    def __init__(self, width=600, height=600, bg_color="AliceBlue", title="Snake Game", speed=100):
        """
        Initialize screen, snake, food, scoreboard, and controls.

        Args:
            width (int): Screen width.
            height (int): Screen height.
            bg_color (str): Background color.
            title (str): Window title.
            speed (int): Movement delay in milliseconds.
        """
        self._screen = Screen()
        self._screen.setup(width=width, height=height)
        self._screen.bgcolor(bg_color)
        self._screen.title(title)
        self._screen.tracer(0)

        self._snake = Snake()
        self._food = Food()
        self._scoreboard = Scoreboard()
        self._speed = speed  # milliseconds
        self._paused = False

        self._setup_controls()
        self._screen.ontimer(self._game_loop, self._speed)

    def _setup_controls(self):
        """Bind arrow keys for snake movement and space for restart."""
        self._screen.listen()
        self._screen.onkey(self._snake.up, "Up")
        self._screen.onkey(self._snake.down, "Down")
        self._screen.onkey(self._snake.left, "Left")
        self._screen.onkey(self._snake.right, "Right")
        self._screen.onkey(self._unpause, "space")

    def _unpause(self):
        """Unpause after game over."""
        if self._paused:
            self._paused = False
            self._snake.reset()
            self._scoreboard.reset()

    def _check_collisions(self):
        """Check collisions and handle game over."""
        if self._food.distance_to(self._snake.head) < 15:
            self._food.refresh()
            self._snake.extend()
            self._scoreboard.increase_score()

        if self._snake.collided_with_wall() or self._snake.collided_with_self():
            self._scoreboard.game_over(self._screen)
            self._paused = True

    def _game_loop(self):
        """Asynchronous game loop using ontimer."""
        if not self._paused:
            self._snake.move()
            self._check_collisions()
            self._screen.update()
        self._screen.ontimer(self._game_loop, self._speed)

    @property
    def screen(self):
        """Access the Screen object."""
        return self._screen
