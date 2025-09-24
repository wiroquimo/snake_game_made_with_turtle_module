"""
scoreboard.py

Manages the display of score and game-over messages in a fully asynchronous manner.
"""

from turtle import Turtle


class Scoreboard:
    """Manages and displays the player's score and game-over messages."""

    def __init__(self):
        """Initialize hidden turtle and starting score."""
        self._turtle = Turtle()
        self._turtle.color("black")
        self._turtle.penup()
        self._turtle.hideturtle()
        self._turtle.goto(0, 265)
        self._score = 0
        self._blinking = False
        self._prompt_visible = False
        self._update_scoreboard()

    def _update_scoreboard(self):
        """Redraw the score at the top of the screen."""
        self._turtle.clear()
        self._turtle.goto(0, 265)
        self._turtle.write(f"Score: {self._score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increase score by 1 and update display."""
        self._score += 1
        self._update_scoreboard()

    def game_over(self, screen):
        """
        Display 'GAME OVER' and start blinking restart prompt asynchronously.
        
        Args:
            screen (Screen): Turtle screen for scheduling blinking.
        """
        self._turtle.clear()
        self._turtle.goto(0, 0)
        self._turtle.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
        self._turtle.goto(0, -40)
        self._turtle.write(f"Final Score: {self._score}", align="center", font=("Arial", 20, "normal"))

        # Start blinking asynchronously
        self._blinking = True
        screen.ontimer(lambda: self._blink(screen), 500)

    def _blink(self, screen):
        """Blink the restart message asynchronously."""
        if not self._blinking:
            return

        # toggle visibility
        self._turtle.goto(0, -80)
        if self._prompt_visible:
            self._turtle.clear()  # clear restart message
            self._prompt_visible = False
        else:
            self._turtle.write("Press space key to restart", align="center", font=("Arial", 16, "italic"))
            self._prompt_visible = True

        # schedule next blink
        screen.ontimer(lambda: self._blink(screen), 500)

    def reset(self):
        """Stop blinking, reset score, and redraw scoreboard."""
        self._blinking = False
        self._score = 0
        self._prompt_visible = False
        self._turtle.clear()
        self._update_scoreboard()

    @property
    def score(self):
        """Read-only property for current score."""
        return self._score
