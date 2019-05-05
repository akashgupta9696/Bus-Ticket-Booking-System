from Tkinter import *
import os

root=Tk()
root.title("Welcome")
def pro():
    import project
def enq():
    import enquiry
Label(root,text="WELCOME USERS",bg="red",font="times 30 bold",bd=7).grid()
Button(root,text='BOOKING',command=pro,bd=7,bg="blue",fg="white",font="bold").grid(row=1,column=0)
Button(root,text='ENQUIRY',command=enq,bd=7,bg="powder blue",font="bold").grid(row=2,column=0)

root.mainloop()
