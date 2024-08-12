from turtle import Turtle, Screen
import random
import colorgram

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy.color("red")

# for i in range(4):
#     timmy.forward(100)  
#     timmy.left(90)

# for i in range(15):
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)
#     timmy.down()

def get_deg(number_sides):
    return 360/number_sides
def draw_line():
    timmy.forward(100)
def change_color():
    timmy.color(random.choice(colours))

# shapes
# for shape in range(3,11):
#     change_color()
#     for sides in range(shape):
#         deg = get_deg(shape)
#         draw_line()
#         timmy.right(deg)

def get_true_random_color():
    #  col = tuple(random.randint(1,255) for _ in range(3))
     r = random.randint(1,255)
     g = random.randint(1,255)
     b = random.randint(1,255)
     ranodm_color = (r,g,b)
     return ranodm_color
    #  timmy.pencolor(col)
     

directions = [0,90,180,270]
def random_direction():
    return random.choice(directions)

#random walk
# timmy.speed("fastest")
# timmy.width(20)
# for i in range(200):
#     timmy.color(get_true_random_color())
#     timmy.setheading(random_direction())
#     timmy.forward(30)

# circle spirograph
def draw_spirogprah(size_of_gap):
    timmy.speed("fastest")
    for i in range(int(360/size_of_gap)):
        timmy.color(get_true_random_color())
        timmy.circle(100)
        # timmy.right(get_deg(100))
        timmy.setheading(timmy.heading() + size_of_gap)

def get_colors_from_image():
    color_list_tuple = []
    colors = colorgram.extract("Day18 turtle_art\hirst_spot_painting.jpg",10)
    # print(colors)
    for entry in colors:
        color_list_tuple.append((entry.rgb[0],entry.rgb[1],entry.rgb[2]))

    print(color_list_tuple)


# get_colors_from_image()
# draw_spirogprah(5)

color_list = [(236, 35, 108), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47)]

def main():
    timmy.hideturtle()
    timmy.width(20)
    timmy.teleport(-400,-400)
    for x in range(10):
        for y in range(10):
            color = random.choice(color_list)
            timmy.dot(50, color)
            timmy.teleport(y=timmy.pos()[1] + 90)
        timmy.teleport(x = timmy.pos()[0] + 90, y = -400)







main()


screen.exitonclick()