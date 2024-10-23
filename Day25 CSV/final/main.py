import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = ".\\Day25 CSV\\final\\blank_states_img.gif"
screen.addshape(image)
screen.setup(725,491)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

right = []
game_is_on = True

data = pandas.read_csv(r"Day25 CSV\final\50_states.csv")
state_names = data["state"].to_list()
# print(state_names)
writer = turtle.Turtle()
writer.pu()
writer.hideturtle()
writer.color("Black")

def write_guess(data,state):
    # print(data)
    guess = data[data["state"] == state]
    name = state
    x_cor = guess["x"].values[0]
    y_cor = guess["y"].item()
    print(type(x_cor), x_cor)
    writer.goto((x_cor,y_cor))
    writer.write(name)

while game_is_on:

    answer_state = screen.textinput(title=f"{len(right)}/50 States Correct", prompt=" What's another state's name?")
    
    if len(right) >= 50:
        print("You won!")
        game_is_on = False

    if answer_state.lower() in (state.lower() for state in state_names) and answer_state.lower() not in (state.lower() for state in right):
        right.append(answer_state.title())
        write_guess(data,answer_state.title())
        
    print(right)

    if answer_state == "exit":
        break

print("exited")

missing_states = []
for state in state_names:
    if state not in right:
        missing_states.append(state)
print(len(missing_states))

new_data = pandas.DataFrame(missing_states)
new_data.to_csv(".\\Day25 CSV\\final\\states_to_learn.csv")