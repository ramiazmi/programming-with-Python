import tkinter
from tkinter import Button, Checkbutton, IntVar, messagebox


def buttonCallBack():
    selected = []
    vars = [CheckVar1, CheckVar2]
    vals = ['Science', 'Technology']
    for i, v in enumerate(vars):
        if v.get() == 1:
            selected.append(vals[i])
    print('Selected: ', selected)
    messagebox.showinfo('Selected Checkbuttons', str(selected))


top = tkinter.Tk()
top.geometry('300x200')

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text="Science", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)
C2 = Checkbutton(top, text="Technology", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)
C1.grid()
C2.grid()

B = Button(top, text="Submit", command=buttonCallBack)
B.place(x=150, y=100)

top.mainloop()
