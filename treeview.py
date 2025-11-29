import sqlite3 as sq
from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Tree view")
frame=LabelFrame(root,text="View Records",height=200,width=800)
frame.pack(padx=10,pady=10)
tree=ttk.Treeview(frame,columns=("rollno","name","city"),show="headings")

tree.heading("rollno",text="rollno")
tree.heading("name",text="name")
tree.heading("city",text="city")

tree.column("rollno",width=200)
tree.column("name",width=200)
tree.column("city",width=200)
tree.pack(fill="both",padx=10,pady=10)

def view_record():
    con=sq.connect("MY.db")
    cur=con.cursor()
    cur.execute("select * from stud")
    rows=cur.fetchall()
    for row in rows:
        tree.insert("",END,values=row)
    con.commit()
    cur.close()
    con.close()
view_record()
#f=tree.selection()
#hs=tree.item(f[0])["values"]

frame1=LabelFrame(root,text="update Records",height=200,width=800)
frame1.pack(padx=10,pady=10)

ven1=IntVar()
ven2=StringVar()
ven3=StringVar()

en1=Entry(frame1,textvariable=ven1)
en1.place(x=20,y=20)

en2=Entry(frame1,textvariable=ven2)
en2.place(x=20,y=40)

en3=Entry(frame1,textvariable=ven3)
en3.place(x=20,y=60)

def update():
    f=tree.selection()
    fh=tree.item(f[0])["values"]
    ven1.set(fh[0])
    ven2.set(fh[1])
    ven3.set(fh[2])
    en3.insert(0,fh[2])


bt1=Button(frame1,text="update",command=update)
bt1.place(x=20,y=100)

root.geometry("700x700")
root.mainloop()