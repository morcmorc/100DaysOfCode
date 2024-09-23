from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_clockwise():
    tim.right(10)

def turn_counterclockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()
    

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
