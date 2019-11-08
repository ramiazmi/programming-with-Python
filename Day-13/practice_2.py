import re
import tkinter
from tkinter import messagebox, Button, Entry, Label, LEFT, RIGHT


def validate_email():
    email = E.get()
    if email:
        result = 'Right Email' if re.match('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email) else 'Wrong'
        label.config(text=result)
    else:
        msg = messagebox.showinfo("Alert Message", "Please, enter an email .. !")


def validate_mobile_number():
    mobile_number = E2.get()
    if mobile_number:
        result = 'Right Number' if re.match('^059[1-9]{1}([0-9]{6})$', mobile_number) else 'Wrong'
        label2.config(text=result)
    else:
        msg = messagebox.showinfo("Alert Message", "Please, enter an Jawwal mobile number .. !")


top = tkinter.Tk()
top.geometry('400x150')

# Email Validation
L = Label(top, text="Email:")
L.place(x=1, y=20)
E = Entry(top)
E.place(x=50, y=20)
B = Button(top, text="Submit", command=validate_email)
B.place(x=220, y=20)
label = Label(top)
label.place(x=200, y=50)

# Jawwal Number Validation
L2 = Label(top, text="Mobile:")
L2.place(x=1, y=70)
E2 = Entry(top)
E2.place(x=50, y=70)
B2 = Button(top, text="Submit", command=validate_mobile_number)
B2.place(x=220, y=70)
label2 = Label(top)
label2.place(x=200, y=100)

top.mainloop()
