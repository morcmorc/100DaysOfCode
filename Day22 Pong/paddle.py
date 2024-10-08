from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self,player) -> None:
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if player == "left":
            self.teleport(-350,0)
        else:
            self.teleport(350,0)
        

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)