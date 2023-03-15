from turtle import Turtle

STARTING_POSITION = (0,-380)
MOVE_DISTANCE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_finish(self):
        if self.ycor() > 380:
            return True
        else:
            return False

    def start_over(self):
        self.goto(STARTING_POSITION)




