import tkinter
from tkinter import Label, IntVar, Radiobutton, StringVar, W

top = tkinter.Tk()
top.geometry('300x400')


def button_selected():
    selection = "You chose {}".format(var.get())
    label.config(text=selection)


var = StringVar()
R1 = Radiobutton(top, text="Arabic", variable=var, value='Arabic', command=button_selected)
R1.pack(anchor=W)
R2 = Radiobutton(top, text="English", variable=var, value='English', command=button_selected)
R2.pack(anchor=W)
R3 = Radiobutton(top, text="Turkish", variable=var, value='Turkish', command=button_selected)
R3.pack(anchor=W)
label = Label(top)
label.pack()

top.mainloop()
