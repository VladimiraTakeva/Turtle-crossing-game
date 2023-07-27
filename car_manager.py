from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.start_position = 280
        self.move_speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()

            y = random.randint(-250, 250)
            new_car.color(random.choice(COLORS))
            new_car.goto(self.start_position, y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.move_speed)

    def detect_collision(self, turtle):
        for car in self.cars:
            if turtle.distance(car) < 20:
                return True

    def level_up(self):
        self.move_speed += MOVE_INCREMENT








