from turtle import Turtle
import random

COLORS = ["red", "blue", "orange", "green", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    """Creates and manages cars."""

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Randomly create a new car."""
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move_cars(self):
        """Move all cars left."""
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        """Increase car speed."""
        self.speed += MOVE_INCREMENT
