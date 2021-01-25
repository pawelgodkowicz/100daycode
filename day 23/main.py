import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

jim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(jim.goup, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if jim.distance(car) < 20:
            scoreboard.gameover()
            game_is_on = False

    if jim.crose_the_road():
        jim.go_to_start()
        scoreboard.update_scoretable()
        car_manager.increase_speed()

screen.exitonclick()
