import tkinter
from tkinter import messagebox, Button, Entry, Label, LEFT, RIGHT

top = tkinter.Tk()
top.geometry('300x400')

L = Label(top, text="Name:")
L.pack(side=LEFT)
E = Entry(top, bd=3)
E.pack(side=RIGHT)

top.mainloop()
