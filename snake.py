"""
snake.py

Represents the snake in the game.
"""

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Represents the snake in the game."""

    def __init__(self):
        """Create a new snake with initial segments."""
        self._segments = []
        self._create_snake()
        self._head = self._segments[0]

    def _create_snake(self):
        """Create initial snake body segments."""
        for position in STARTING_POSITIONS:
            self._add_segment(position)

    def _add_segment(self, position):
        """Add a segment at the given position (internal use)."""
        segment = Turtle("square")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self._segments.append(segment)

    def reset(self):
        """Clear current snake and start a new one in the center."""
        for seg in self._segments:
            seg.goto(1000, 1000)  # move off-screen
        self._segments.clear()
        self._create_snake()
        self._head = self._segments[0]

    def extend(self):
        """Add a new segment at the end of the snake."""
        self._add_segment(self._segments[-1].position())

    def move(self):
        """Move the snake forward one step."""
        for seg_num in range(len(self._segments) - 1, 0, -1):
            new_x = self._segments[seg_num - 1].xcor()
            new_y = self._segments[seg_num - 1].ycor()
            self._segments[seg_num].goto(new_x, new_y)
        self._head.forward(MOVE_DISTANCE)

    def up(self):
        if self._head.heading() != DOWN:
            self._head.setheading(UP)

    def down(self):
        if self._head.heading() != UP:
            self._head.setheading(DOWN)

    def left(self):
        if self._head.heading() != RIGHT:
            self._head.setheading(LEFT)

    def right(self):
        if self._head.heading() != LEFT:
            self._head.setheading(RIGHT)

    def collided_with_wall(self):
        """Return True if snake hits the wall boundaries."""
        x, y = self._head.xcor(), self._head.ycor()
        return x > 280 or x < -280 or y > 280 or y < -280

    def collided_with_self(self):
        """Return True if snake collides with its own body."""
        for segment in self._segments[1:]:
            if self._head.distance(segment) < 10:
                return True
        return False

    @property
    def head(self):
        """Read-only property to expose the snake's head."""
        return self._head
