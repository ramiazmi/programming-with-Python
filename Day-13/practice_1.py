import tkinter
from tkinter import messagebox, Button, Entry, Label, LEFT, RIGHT


def buttonCallBack():
    entry_text = E.get()
    if entry_text:
        msg = messagebox.showinfo("Welcome Message", "Hi {}".format(entry_text))
    else:
        msg = messagebox.showinfo("Alert Message", "Please, fill the Name field .. !")



top = tkinter.Tk()
top.geometry('200x150')

L = Label(top, text="Name:")
L.pack(side=LEFT)
E = Entry(top)
E.pack(side=RIGHT)
B = Button(top, text="Submit", command=buttonCallBack)
B.place(x=130, y=90)

top.mainloop()
