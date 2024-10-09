from turtle import Turtle       

LEFT = 180
RIGHT = 0

class Car(Turtle):
    def __init__(self,color,x,y):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.seth(LEFT)
        self.pu()
        self.goto((x,y))
        self.shapesize(1,2)

    def move(self,dist):
        self.forward(dist)
    
    def respawn(self,c,x,y):
        self.color(c)
        self.goto((x,y))