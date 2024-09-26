from turtle import Turtle

from regex import F

ALIGMENENT = "center"
FONT = ("Courier",15,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0,270)
        self.score = 0
        self.update()

    def increase(self):
        self.score += 1
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGMENENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGMENENT, font=FONT)