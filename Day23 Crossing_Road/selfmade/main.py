from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.move,"w")


#methodes
def checkFinish():
    if player.ycor() >= 250:
        player.restart()
        scoreboard.increase()

def checkCollision():
    global game_is_on
    for car in car_manager.car_list:
        if player.distance(car) <= 20:
            # print(f"{game_is_on}")
            scoreboard.game_over()
            game_is_on = False

while game_is_on:
    time.sleep(0.1)
    screen.update()

    scoreboard.update()
    car_manager.update()

    checkFinish()
    checkCollision()



screen.exitonclick()