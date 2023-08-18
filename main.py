from turtle import Screen
import time
from timmy import Timmy
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)


timmy = Timmy()
cars = Cars()
score = Scoreboard()

screen.listen()
screen.onkey(timmy.up, "Up")
screen.onkey(timmy.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_a_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            score.game_over()

    if timmy.ycor() > 290:
        timmy.reset()
        score.increase_level()
        cars.increase_speed()


screen.exitonclick()
