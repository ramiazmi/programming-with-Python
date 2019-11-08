import tkinter
from tkinter import Button


def buttonCallBack():
    print('Button clicked ... !')


top = tkinter.Tk()
top.geometry('300x200')

B = Button(top, text="Submit", command=buttonCallBack)
B.place(x=150, y=100)

top.mainloop()
