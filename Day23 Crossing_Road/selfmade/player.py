from turtle import Turtle

UP = 90
SPEED = 2

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.goto((0,-200))
        self.seth(UP)

    def move(self):
        self.forward(SPEED)