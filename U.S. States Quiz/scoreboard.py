from turtle import Turtle

FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}/50 ", align="left", font=FONT)
