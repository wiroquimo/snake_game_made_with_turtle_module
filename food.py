"""
food.py

Represents the food object in the snake game.
"""

from turtle import Turtle
import random


class Food:
    """Represents the food item in the snake game."""

    def __init__(self):
        """Initialize a black circle turtle at a random position."""
        self._turtle = Turtle("circle")
        self._turtle.penup()
        self._turtle.color("black")
        self._turtle.shapesize(stretch_len=1, stretch_wid=1)
        self.refresh()

    def refresh(self):
        """Move the food to a new random location on the screen."""
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self._turtle.goto(x, y)

    def distance_to(self, other):
        """Return distance to another turtle-like object or position."""
        return self._turtle.distance(other)

    @property
    def position(self):
        """Read-only property for food's current position."""
        return self._turtle.position()
