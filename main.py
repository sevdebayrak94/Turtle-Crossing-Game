import time
from os import supports_dir_fd
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scores = Scoreboard()
screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_segments()
    car_manager.movement()

    #Detect Collision with cars wall
    for car in car_manager.all_cars:
       if car.distance(player) < 20:
           game_is_on = False
           scores.game_over()

    #Level up
    if player.finish_line():
        player.start_again()
        car_manager.level_up()
        scores.increase_level()



screen.exitonclick()