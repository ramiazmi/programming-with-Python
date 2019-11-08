import tkinter
from tkinter import messagebox, Button, Entry, Label, LEFT, RIGHT, IntVar, Checkbutton, Listbox

top = tkinter.Tk()
top.geometry('300x400')

LB1 = Listbox(top)
LB1.insert(1, "Al-Quds")
LB1.insert(2, "Nablus")
LB1.insert(3, "Hebron")
LB1.insert(4, "Beitlahem")
LB1.insert(4, "Jenin")
LB1.pack()

top.mainloop()
