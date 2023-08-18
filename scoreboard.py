from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.increase_level()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))

    def increase_level(self):
        self.clear()
        self.penup()
        self.goto(x=-240, y=260)
        self.level += 1
        self.write(f"LEVEL : {self.level}", align="center", font=("Verdana", 15, "normal"))
