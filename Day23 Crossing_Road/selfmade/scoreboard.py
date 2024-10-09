from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("black")
        self.pu()
        self.hideturtle()
        self.level = 0

    def update(self):
        self.clear()
        self.goto((-200,250))
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))

    def increase(self):
        self.level += 1
        self.update()
    
    def reset(self):
        self.level = 0
        self.update()

    def game_over(self):
        self.goto ((0,0))
        self.write(f"Game Over!", align="center", font=("Courier", 20, "normal"))