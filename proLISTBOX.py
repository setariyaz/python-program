import sqlite3 as sq
from tkinter import *
from tkinter import messagebox,ttk  

root=Tk()
root.title("LIST BOX EXAMPLE")


def init():
    con=sq.connect("STUD.db")
    cur=con.cursor()
    cur.execute("create table if not exists student(id integer primary key autoincrement,name text,city text,sem text,number text)")
    cur.close()
    con.close()
init()

fram1=LabelFrame(root,text="INSERT RECORDS",height=400,width=700,font="bold")
fram1.pack()

heading=Label(fram1,text="STUDENT INFORMATION",font="bold")
heading.place(x=250,y=10)

lb1=Label(fram1,text="STUDENT NAME")
lb1.place(x=30,y=50)
e1=Entry(fram1)
e1.place(x=140,y=50)

lb2=Label(fram1,text="CITY")
lb2.place(x=30,y=80)
e2=Entry(fram1)
e2.place(x=140,y=80)

abc=StringVar(value="SELECT")
lb3=Label(fram1,text="SEM")
lb3.place(x=30,y=110)
e3=ttk.Combobox(fram1,width=17,values=("SEM-1","SEM-2","SEM-3","SEM-4","SEM-5","SEM-6"),textvariable=abc)
e3.place(x=140,y=110)


lb4=Label(fram1,text="NUMBER")
lb4.place(x=30,y=140)
e4=Entry(fram1)
e4.place(x=140,y=140)

list1=Listbox(fram1)
list1.place(x=400,y=50)

def add():
    nm=e1.get()
    ct=e2.get()
    sm=e3.get()
    num=e4.get()

    if(nm=="" or ct=="" or sm=="SELECT" or num==""):
        messagebox.showerror("error","please enter the field")
    else:
        con=sq.connect("STUD.db")
        cur=con.cursor()
        cur.execute("insert into student(name,city,sem,number) values(?,?,?,?)",(nm,ct,sm,num))
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo("information","record inserted")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.set("SELECT")
        e4.delete(0,END)
        list1.insert(END,nm)

def studinsert():
    con=sq.connect("STUD.db")
    cur=con.cursor()
    cur.execute("select name from student")
    row=cur.fetchall()
    for rows in row:
        list1.insert(END,rows)
    con.commit()
    cur.close()
    con.close()
studinsert()

    




btn1=Button(fram1,text="ADD",command=add)
btn1.place(x=140,y=170)


fram2=LabelFrame(root,text="VIEW RECORDS",height=400,width=700,font="bold")
fram2.pack(padx=10)

tree=ttk.Treeview(fram2,columns=("ID","STUDENT NAME","CITY","SEM","NUMBER"),show="headings",)

tree.heading("ID",text="ID")
tree.heading("STUDENT NAME",text="NAME")
tree.heading("CITY",text="CITY")
tree.heading("SEM",text="SEM")
tree.heading("NUMBER",text="NUMBER")


tree.column("ID",width=100)
tree.column("STUDENT NAME",width=150)
tree.column("CITY",width=150)
tree.column("SEM",width=150)
tree.column("NUMBER",width=150)

tree.pack(fill="both",padx=10,pady=10)

def viewrecords():
    select=list1.curselection()
    if not select:
        messagebox.showerror("error","please select data")
    else:
        nm=list1.get(select[0])
        con=sq.connect("STUD.db")
        cur=con.cursor()
        cur.execute("select * from student where name=?",(nm))
        row=cur.fetchall()
        for rows in row:
            tree.insert("",END,values=rows)
        con.commit()
        cur.close()
        con.close()




btn2=Button(fram1,text="VIEW",command=viewrecords)
btn2.place(x=410,y=220)


root.geometry("900x700+10+10")
root.mainloop()