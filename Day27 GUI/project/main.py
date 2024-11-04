from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)


def calc():
    miles = inp.get()
    km = float(miles) * 1.609
    label3.config(text=round(km))

inp = Entry()
inp.config(width=10)
label1 = Label(text="Miles")
label2 = Label(text="is equal to")
label3 = Label(text="0")
label4 = Label(text="Km")
btn = Button(text="Calculate", command=calc)


inp.grid(column=1,row=0)
label1.grid(column=2, row=0)
label2.grid(column=0, row=1)
label3.grid(column=1, row=1)
label4.grid(column=2, row=1)
btn.grid(column=1, row=3)



window.mainloop()
