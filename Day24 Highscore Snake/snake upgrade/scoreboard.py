from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0 
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.get_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.set_highscore()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def get_highscore(self):
        with open ("highscore.txt","r") as file:
            self.highscore = int(file.read())

    def set_highscore(self):
        with open ("highscore.txt","w") as file:
            file.write(str(self.highscore))