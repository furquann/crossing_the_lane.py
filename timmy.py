from turtle import Turtle


class Timmy(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.speed("fastest")
        self.color("black")
        self.penup()
        self.goto(x=0, y=-280)
        self.setheading(90)
        self.showturtle()

    def up(self=None):
        self.forward(10)

    def down(self=None):
        self.forward(-10)

    def reset(self):
        self.goto(x=0, y=-280)
