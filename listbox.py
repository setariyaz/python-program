import sqlite3 as sq
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("COLLAGE WORK")
frame=LabelFrame(root,text="For Record Insert",height=300,width=600)
frame.pack(pady=10)

lbl1=Label(frame,text="NAME")
lbl1.place(x=100,y=30)

txt1=Entry(frame)
txt1.place(x=150,y=30)

lbl2=Label(frame,text="city")
lbl2.place(x=100,y=60)

ct=Listbox(frame, width=22, height=10)
ct.place(x=148,y=60)
ct.insert(END,"junagdh")
ct.insert(END,"kodinar")
ct.insert(END,"jamnagar")
ct.insert(END,"porabandar")
ct.insert(END,"maliya")
ct.insert(END,"gadu")
ct.insert(END,"mangroad")
ct.insert(END,"veraval")
ct.insert(END,"keshod")
def save():
    name = txt1.get()

    # validate name
    if name == "":
        messagebox.showinfo("Validation Error", "Please enter the name")
        return

    # validate city selection
    selected = ct.curselection()
    if not selected:
        messagebox.showinfo("Validation Error", "Please select a city")
        return

    city = ct.get(selected[0])

    # insert into DB
    con = sq.connect("MY.db")
    cur = con.cursor()
    cur.execute("INSERT INTO stud(name, city) VALUES(?, ?)", (name, city))
    con.commit()
    cur.close()
    con.close()

    messagebox.showinfo("Information", "Record Inserted Successfully")

    txt1.delete(0, END)
    refersh_tree()


btn1=Button(frame,text="SAVE",command=save)
btn1.place(x=150,y=230)



frame3=LabelFrame(root,text="View Record",height=200,width=600)
frame3.pack(pady=10)

tree=ttk.Treeview(frame3,columns=("ROLLNO","NAME","CITY"),show="headings")
tree.heading("ROLLNO",text="ROLLNO")
tree.heading("NAME",text="NAME")
tree.heading("CITY",text="CITY")

tree.column("ROLLNO",width=200)
tree.column("NAME",width=200)
tree.column("CITY",width=200)

tree.pack(fill="both",padx=10,pady=10)

def refersh_tree():
    for row in tree.get_children():
        tree.delete(row)
    con=sq.connect("MY.db")
    cur=con.cursor()
    cur.execute("select * from stud")
    rows=cur.fetchall()
    for row1 in rows:
        tree.insert("",END,values=row1)
    con.commit()
    cur.close()
    con.close()


def viewrecord():
    con=sq.connect("MY.db")
    cur=con.cursor()
    members=cur.execute("select * from stud")
    con.commit()
    for member in members:
        tree.insert("",END,values=member)

    cur.close()
    con.close()
   
viewrecord()




root.geometry("1200x1200")
root.mainloop()