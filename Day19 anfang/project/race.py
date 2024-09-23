from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput("Make a guess", "Which color will win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

for color in colors:
    name = color
    print(color)
    name = Turtle(shape="turtle")
    name.color(color)
    name.pu()
    name.goto(x=-230,y=-100+colors.index(color)*50)
    turtle_list.append(name)

if guess:
    is_race_on = True



while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == guess:
                print(f"You won! The {win_color} turtle won!")
                
            else: 
                print(f"You lost! The {win_color} turtle won!")
                

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

    

screen.exitonclick()