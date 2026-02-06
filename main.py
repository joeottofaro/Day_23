import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating our objects
player = Player()
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()

# Key binding to move the player up
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    # Detect if player hits a car
    for cars in car_manager.car_list:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    # Detect if player crosses the finish line(Top of the screen)
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
