from Tkinter import *
from tkMessageBox import *
from random import *
import sqlite3
root=Tk()
root.title("Reservation Window")

con=sqlite3.Connection('infodb')
cur=con.cursor()
cur.execute("create table if not exists bus(bus_pnr number primary key,fname varchar(20),lname varchar(20),dob date,doj date,phone_no number,destinat varchar(20),sex varcha2(20),age number,berth number,board number)")

cur.execute("create table if not exists seat1(bus_no number,seat number primary key,status varchar(20))")
'''i=1
while(i<41):
    cur.execute("insert into seat1(seat) values(?)",[i])
    con.commit()
    i=i+1'''


Label(root,text="WELCOME TO ONLINE BUS RESERVATION SYSTEM",bd=7,font="times 30 bold",bg="purple",fg="white").grid(row=0,column=0,columnspan=5)
Label(root,text="BUS Name or No. :",font="times 15 bold").grid(row=1,column=0)
v0=Entry(root,bg="powder blue")
v0.grid(row=1,column=1)
Label(root,text="First Name :",font="times 15 bold").grid(row=2,column=0)
v1=Entry(root,bg="powder blue")
v1.grid(row=2,column=1)
Label(root,text="Last Name :",font="times 15 bold").grid(row=3,column=0)
v2=Entry(root,bg="powder blue")
v2.grid(row=3,column=1)
Label(root,text="DOB :",font="times 15 bold").grid(row=4,column=0)
v3=Entry(root,bg="powder blue")
v3.grid(row=4,column=1)
Label(root,text="Date of Journey :",font="times 15 bold").grid(row=6,column=0)
v4=Entry(root,bg="powder blue")
v4.grid(row=6,column=1)
Label(root,text="Mobile no. :",font="times 15 bold").grid(row=7,column=0)
v5=Entry(root,bg="powder blue")
v5.grid(row=7,column=1)
Label(root,text="Destination :",font="times 15 bold").grid(row=1,column=2)
v6=Entry(root,bg="powder blue")
v6.grid(row=1,column=3)
Label(root,text="Sex :",font="times 15 bold").grid(row=3,column=2)
v7=Entry(root,bg="powder blue")
r1=Radiobutton(root,text='MALE',variable=v7,value=1).grid(row=3,column=3)
r2=Radiobutton(root,text='FEMALE',variable=v7,value=2).grid(row=3,column=4)
Label(root,text="Age :",font="times 15 bold").grid(row=4,column=2)
v8=Entry(root,bg="powder blue")
v8.grid(row=4,column=3)
Label(root,text="Berth :",font="times 15 bold").grid(row=5,column=2)
v9=Entry(root,bg="powder blue")
r11=Radiobutton(root,text='Upper',variable=v9,value=1).grid(row=5,column=3)
r12=Radiobutton(root,text='Lower',variable=v9,value=2).grid(row=5,column=4)
Label(root,text="Boarding Station :",font="times 15 bold").grid(row=6,column=2)
v10=Entry(root,bg="powder blue")
v10.grid(row=6,column=3)
def insert():
    g=v0.get()
    cur.execute('select fname from bus where bus_pnr=?',(int(g),))
    f=cur.fetchall()
    if len(f)>0:
        showerror('wrong','duplicate info')
    else:
        cur.execute("insert into bus values(?,?,?,?,?,?,?,?,?,?,?)",(v0.get(),v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get(),v10.get()))
        dic=(v0.get(),v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get(),v10.get())
        con.commit()
        v0.delete(0,END)
        v1.delete(0,END)
        v2.delete(0,END)
        v3.delete(0,END)
        v4.delete(0,END)
        v5.delete(0,END)
        v6.delete(0,END)
        v7.delete(0,END)
        v8.delete(0,END)
        v9.delete(0,END)
        v10.delete(0,END)
        showinfo('inserted info',dic)


def showall():
    cur.execute('select * from bus',())
    w=cur.fetchall()
    showinfo('every info',w)

def call(x):
    root=Toplevel()
    a=cur.execute("select * from seat1 where seat =?",(x,)).fetchall()
    if a[0][2]=='o':
        showerror('error','SORRY!!!! The seat is currently occupied ')
    else:
        Label(root,text = "Enter bus number").grid(row=1,column=0,sticky=W)
        y= Entry(root)
        y.grid(row=1,column=1)
    def insert():
        cur.execute("update seat1 set status=?,bus_no=? where seat=?",("o",int(y.get()),x)).fetchall()
        con.commit()
    Button(root,text='Insert',fg='black',bg='turquoise',font='times 12 bold',bd=5,command=insert).grid(row=3,column=0)
    Button(root,text='Exit',fg='black',bg='turquoise',font='times 12 bold',bd=5,command=root.destroy).grid(row=3,column=1)
    def details():
        root=Toplevel()
        cur.execute('select * from bus where bus_pnr=(?)',[int(y.get())])
        Label(root,text=" your seat number is          :"+str(x),font='times 12 bold italic',fg='brown').grid(row=13,column=0,sticky=W)
    Button(root,text='DETAIL',font='times 15 bold italic',bd=5,fg='black',bg='blue',command=details).grid(row=5,sticky=N)


z=randint(1,40)
Button(root,text="SUBMIT",bg="light green",fg="black",bd=7,font="bold",command=insert).grid(row=8,column=0)
Button(root,text="BOOK",bg="light green",fg="black",bd=7,font="bold",command=lambda:call(z)).grid(row=8,column=1)
Button(root,text="CANCEL",bg="red",bd=7,font="bold",command=root.destroy).grid(row=8,column=2)
Button(root,text="SHOW ALL",bg="red",bd=7,font="bold",command=showall).grid(row=8,column=3)





root.mainloop()
