import tkinter as t
import sqlite3 as sq
root=t.Tk()
root.title("INSERT")

lb=t.Label(root,text="rollno")
lb.place(x=10,y=20)

txt=t.Entry(root)
txt.place(x=50,y=20)


lb1=t.Label(root,text="name")
lb1.place(x=10,y=50)

var1=t.StringVar()
txt1=t.Entry(root,textvariable=var1)
txt1.place(x=50,y=50)

lb2=t.Label(root,text="city")
lb2.place(x=10,y=80)

var2=t.StringVar()
txt2=t.Entry(root,textvariable=var2)
txt2.place(x=50,y=80)

def get():
    con=sq.connect("MY.db")
    cur=con.cursor()
    cur.execute("insert into stud(name,city)values(?,?)",(txt1.get(),txt2.get()))
    lb3.config(text="Record Insert Successfully")
    con.commit()
    cur.close()
    con.close()


btn1=t.Button(root,text="INSERT",command=get)
btn1.place(x=50,y=110)

def update():
    con=sq.connect("MY.db")
    cur=con.cursor()
    cur.execute("update stud set name=?,city=? where rollno=?",(txt1.get(),txt2.get(),txt.get()))
    lb3.config(text="Record update Successfully")
    con.commit()
    cur.close()
    con.close()

btn2=t.Button(root,text="UPDATE",command=update)
btn2.place(x=110,y=110)

def delete():
    con=sq.connect("MY.db")
    cur=con.cursor()
    cur.execute("delete from stud where rollno=?",(txt.get(),))
    lb3.config(text="Record delete Successfully")
    con.commit()
    cur.close()
    con.close()

btn3=t.Button(root,text="DELETE",command=delete)
btn3.place(x=170,y=110)

def search():
    con=sq.connect("MY.db")
    cur=con.cursor()
    cur.execute("select * from stud where rollno=?",(txt.get(),))
    rows=cur.fetchone()
    var1.set(rows[1])
    var2.set(rows[2])
    con.commit()
    cur.close()
    con.close()


btn4=t.Button(root,text="SEARCH",command=search)
btn4.place(x=190,y=20)

lb3=t.Label(root,text="?")
lb3.place(x=50,y=140)
root.geometry("700x700")
root.mainloop()