from turtle import Turtle

UP = 90
SPEED = 6

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.seth(UP)
        self.restart()

    def move(self):
        self.forward(SPEED)
    
    def restart(self):
        self.goto((0,-200))
        