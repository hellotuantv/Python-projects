from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

#screen setup
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up") # you can only move up for this game

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_left()
    for car in cars.cars:
        if car.distance(player) < 20: # turtle hit the car
            game_is_on = False
            scoreboard.game_over()

    if player.is_finish(): # turtle reach the goal
        player.start_over()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()




