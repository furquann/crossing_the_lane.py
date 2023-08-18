import turtle
from turtle import Turtle
from random import *

turtle.colormode(255)
SPEED_INCREMENT = 5


def color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


class Cars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = SPEED_INCREMENT
        self.level = 1
        self.cars_random = 6

    def create_a_car(self):
        random_chance = randint(1, self.cars_random)
        if random_chance == 1:
            car = Turtle()
            turtle.colormode(255)
            car.hideturtle()
            car.color(color())
            car.penup()
            car.goto(x=310, y=randint(-250, 250))
            car.shape("square")
            car.turtlesize(stretch_len=2)
            car.setheading(180)
            car.speed("fastest")
            car.showturtle()
            car.setheading(180)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            if car.xcor() > -320:
                car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += SPEED_INCREMENT
        self.level += 1
        if self.level == self.level % 5:
            if self.level > 2:
                self.cars_random -= 1
