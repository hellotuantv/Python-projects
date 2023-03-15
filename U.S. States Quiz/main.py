from states import States
from state import State
from scoreboard import Scoreboard
import turtle
import time

#screen setup
screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.tracer(0)
states = States()
scoreboard = Scoreboard()
screen.update()

game_is_on = True

while scoreboard.score < 50 and game_is_on: # game won't stop until you get all 50 states
    time.sleep(0.1)
    screen.update()
    for state in states.states:
        if state.is_finished():
            game_is_on = False
        elif state.is_listed_map() and not state.is_counted():
            scoreboard.score += 1
            scoreboard.write_scoreboard()
            screen.update()
            state.is_scored = True





