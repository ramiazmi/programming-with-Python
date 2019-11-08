import tkinter
from tkinter import messagebox, Button, Entry, Label, LEFT, RIGHT, IntVar, Checkbutton

top = tkinter.Tk()
top.geometry('300x400')

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text="Pizza", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)
C2 = Checkbutton(top, text="Fries", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)
C1.pack()
C2.pack()

top.mainloop()
