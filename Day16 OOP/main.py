# import turtle
# # import another_moduel
# # print(another_moduel.another_variable)

# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


# Pipes
print("| Pokemon Name | Type |")
print("------------------------")

from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
# table = PrettyTable()
table = ColorTable(theme=Themes.OCEAN)

table.field_names = ["Pokemon Name","Type","Level"]
table.add_row(["schiggy","wasser","61"])
table.add_rows(
    [
        ["mew","psycho","12"],
        ["baum","erde","71"]
    ]
)
table.align = "l"

print(table)