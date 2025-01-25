FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.penup()
        self.goto(0,276)
        self.write(f"Level: {self.score}", align="center", font=("Arial", 18, "normal"))
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
    def level(self):
        self.penup()
        self.goto(0,276)
        self.color("black")
        self.write(f"Level: {self.score}", align="center", font=("Arial", 18, "normal"))
    def increase_level(self):
        self.score += 1
        self.clear()
        self.level()



