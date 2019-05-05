from Tkinter import *
import sqlite3
import tkMessageBox
con=sqlite3.connect("busno")
cur=con.cursor()
cur.execute("create table if not exists status(Sno varchar(5) primary key,sour varchar(25),dest varchar(25),time varchar(20))")
cur.execute("insert into status values('1','From- Guna','To- Lucknow','right time')")
cur.execute("insert into status values('2','From- Guna','To- Kanpur','15 min late')")
cur.execute("insert into status values('3','From- Delhi','To- Goa','10 min late')")
cur.execute("insert into status values('4','From- Kanpur','To- Allahabad','right time')")
cur.execute("insert into status values('5','From- Mumbai','To- Kanpur','right time')")
cur.execute("insert into status values('6','From- Puna','To- Nagpur','15 min late ')")
cur.execute("insert into status values('7','From- Allahabad','To- Lucknow','right time')")
cur.execute("insert into status values('8','From- Bina','To- Shimla','1 hour late')")
cur.execute("insert into status values('9','From- Satna','To- Katni','right time')")
cur.execute("insert into status values('10','From- Guna','To- Goa','1 hour 30 min late')")

root=Tk()
root.title("Enquiry")
Label(root,text="BUS ENQUIRY SYSTEM",font="times 25 bold",bg="powder blue").grid(row=0,column=0,columnspan=2)
Label(root,text="BUS PNR No. :",font="times 15 bold").grid(row=1,column=0)
v0=Entry(root,bg="light green")
v0.grid(row=1,column=1)
def sta():
    r=cur.execute('select * from status where Sno=(?)',(v0.get(),)).fetchone()
    tkMessageBox.showinfo("Info",r)
Button(root,text="STATUS",bg="purple",fg="white",bd=7,font="bold",command=sta).grid(columnspan=2)
root.minsize(width=380,height=120)
root.maxsize(width=380,height=120)

root.mainloop()
