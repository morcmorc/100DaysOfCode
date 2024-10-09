from turtle import Screen
from player import Player
from car_manager import CarManager
import time

#screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#while cond
game_is_on = True
#elements
player = Player()
car_manager = CarManager()


screen.listen()
screen.onkeypress(player.move,"w")


while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.update()




screen.exitonclick()