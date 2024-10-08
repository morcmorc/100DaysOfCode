from turtle import Turtle

BALLSPEED = 2

class Ball(Turtle):    
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.pu()

        self.x_speed = 2
        self.y_speed = 2

        self.scored = 0



    def move(self):
        # print(f"x: {self.xcor()} y: {self.ycor()}")
        xcor = self.xcor()
        ycor = self.ycor()
        if ycor == 290:
            self.y_bounce()
        elif ycor == -290:
            self.y_bounce()
        if xcor >= 400 or xcor <= -400:
            if xcor >= 400: 
                self.scored = 1
                self.x_speed = -2
            else:
                self.scored = 2
                self.x_speed = 2
            self.home()
            # self.x_bounce()
        else:
            new_x = xcor + self.x_speed
            new_y = ycor + self.y_speed
            self.goto(new_x, new_y)

    def paddlebounce(self, left_paddle, right_paddle):
        xcor = self.xcor()
        ycor = self.ycor()

        if self.distance(left_paddle) < 50 and xcor < -340:
            self.x_bounce()
        if self.distance(right_paddle) < 50 and xcor > 340:
            self.x_bounce()

    def x_bounce(self):
        self.x_speed *= -1.1
    def y_bounce(self):
        self.y_speed *= -1
    
    def get_scored(self):
        return self.scored
    def reset_scored(self):
        self.scored = 0