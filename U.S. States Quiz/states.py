from turtle import Turtle,Screen
from state import State
import pandas
import time


class States():
    def __init__(self):
        self.states = []
        self.data = pandas.read_csv("50_states.csv")
        self.add_all_locations()

    # add all states to the screen as bullet points
    def add_all_locations(self):
        state_names = self.data.state.to_list()
        for state in state_names:
            new_state = State()
            state_data = self.data[self.data.state == state]
            new_state.goto(int(state_data.x), int(state_data.y))
            self.states.append(new_state)


