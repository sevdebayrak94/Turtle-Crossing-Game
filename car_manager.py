import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.create_segments()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.movement()
    def create_segments(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            self.tim = Turtle("square")
            self.tim.penup()
            self.tim.shapesize(stretch_len=2, stretch_wid=1)
            self.tim.color(random.choice(COLORS))
            random_y = random.randint(-260, 260)
            self.tim.goto(290, random_y)
            self.all_cars.append(self.tim)
    def movement(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT






