import csv
from tkinter import *
from tkinter import ttk,messagebox
import sqlite3 as sq

root=Tk()
root.title("tree view example")

frame=LabelFrame(root,text="insert record",height=200,width=800)
frame.pack(padx=20,pady=20)


name=Label(frame,text="NAME")
name.place(x=20,y=60)
tx2=Entry(frame)
tx2.place(x=70,y=60)


city=Label(frame,text="CITY")
city.place(x=20,y=90)
tx3=Entry(frame)
tx3.place(x=70,y=90)


def init():
    con=sq.connect("MY.db")
    cur=con.cursor()
    cur.execute("create table if not exists student(id integer primary key autoincrement,name text,city text)")
    cur.close()
    con.close()
init()

def insert():
    
    nm=tx2.get()
    ct=tx3.get()
    if(nm=="" or ct==""):
        messagebox.showerror("error","please enter the values")
    else:
        con=sq.connect("MY.db")
        cur=con.cursor()
        cur.execute("insert into student(name,city)values(?,?)",(nm,ct))
        cur.execute("select * from student")
        row=cur.fetchall()
        tree.insert("",END,values=(cur.lastrowid,nm,ct))
        tx2.delete(0,END)
        tx3.delete(0,END)
        messagebox.showinfo("information","RECORD INSERTED")

        with open("data1.csv","w",newline="") as f:
            data=csv.writer(f)
            data.writerow(["ID","NAME","CITY"])
            for rows in row:
                data.writerow(rows)
            
        con.commit()
        cur.close()
        con.close()
       
       
            
            


btn1=Button(frame,text="SAVE",command=insert)
btn1.place(x=70,y=130)



tree=ttk.Treeview(root,columns=("id","name","city"),show="headings")

tree.heading("id",text="ID")
tree.heading("name",text="NAME")
tree.heading("city",text="CITY")

tree.column("id",width=30,anchor=CENTER)
tree.column("name",width=120,anchor=CENTER)
tree.column("city",width=120,anchor=CENTER)

tree.pack(padx=10,pady=10,fill="both")

root.geometry("700x700+70+70")
root.mainloop()