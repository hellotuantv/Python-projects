from turtle import Turtle, Screen
from scoreboard import Scoreboard
import pandas

# each individual state
class State(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.data = pandas.read_csv("50_states.csv")
        self.is_listed = False
        self.is_scored = False
        self.exited = False
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.onclick(self.question)

    # a window popup when you click on a bullet point
    def question(self, x, y):
        state_answer = self.screen.textinput(title="Guess the State", prompt="What's the state name? Type 'exit' if you want to stop!")
        if state_answer in self.data.state.to_list():
            state_data = self.data[self.data.state == state_answer]
            xcor = int(state_data.x)
            ycor = int(state_data.y)
            if self.xcor() == xcor and self.ycor() == ycor:
                self.reset()
                self.ht()
                self.penup()
                self.goto(xcor,ycor)
                self.write(state_answer,font=('Arial', 12, 'normal'))
                self.is_listed = True
        elif state_answer == "exit":
            self.exited = True


    def is_listed_map(self):
        return self.is_listed

    def is_counted(self):
        return self.is_scored

    def is_finished(self):
        return self.exited
