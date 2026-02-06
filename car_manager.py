import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create and return a new car object."""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



