from Tkinter import *
import os
root=Tk()
root.title("WELCOME ALL")
t=PhotoImage(file='red.gif')
Label(root,image=t).pack()

Label(root,text = "AKASH GUPTA ",font="times 30 bold ").pack()
Label(root,text = "161B017 ",font="times 30 bold ").pack()
Label(root,text = "B1",font="times 30 bold ").pack()
Label(root,text = "PYTHON PROJECT ",font="times 30 bold ").pack()
def splash():
    os.startfile("login.py")
root.after(4000,lambda:splash())
root.after(4000,lambda:root.destroy())
root.mainloop()
