from turtle import Turtle

MOVE_DISTANCE = 20
START_POSITION = (0, -270)
FINISH_LINE_Y = 280


class Animal(Turtle):
    """Player-controlled turtle."""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)

    def go_up(self):
        """Move the turtle upward."""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Return turtle to starting position."""
        self.goto(START_POSITION)
