from tkinter import *

window = Tk()
window.title("First GUI Programm")
window.minsize(width=500,height=300)
window.config(padx=20, pady=20)


# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold")) #italic,bold
# my_label.pack()
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="Newer Text", padx=50, pady=50)

# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = Button(text="click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column= 2, row=0)


# Entry 

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

# input.get()


window.mainloop()