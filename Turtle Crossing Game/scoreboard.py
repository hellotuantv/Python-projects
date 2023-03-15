from turtle import Turtle

FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-380,350)
        self.write_scoreboard()

    def increase_level(self):
        self.level += 1
        self.write_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center",font=FONT)

    def write_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} ", align="left", font=FONT)