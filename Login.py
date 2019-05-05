from Tkinter import *
import sqlite3
from tkMessageBox import *
import os
root=Tk()
root.title("TRAVELING APP")
con=sqlite3.Connection("database")
cur=con.cursor()
diction={"pas":"locked"}
diction["pas"]="password"
def func():
    if password.get()==diction["pas"]:
       showinfo("LOGIN PAGE","Successful")
       os.startfile("select.py")
       #root2.mainloop()
    else:
        showinfo("LOGIN PAGE","Wrong Password")
        

#def change()
Label(root,text = " Bus Reservation System",font="times 30 bold ",bg="light green",fg="white").grid(columnspan=4)
name=Label(root,text = "USER_NAME :",bd=7,).grid(row=1,column=0)
passw=Label(root,text = "PASSWORD :",bd=7).grid(row=2,column=0)
uname = Entry(root,bg="powder blue")
uname.grid(row=1,column=1)
password = Entry(root,show="*",bg="red")
password.grid(row=2,column=1)
Button(root,text='LOGIN',command=func,bg="black",fg="white",bd=7).grid(row=7,column=1)



root.mainloop()

