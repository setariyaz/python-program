import tkinter as t
import sqlite3 as sq
root=t.Tk()
root.title("INSERT")
con=sq.connect("MY.db")
cur=con.cursor()
cur.execute("select * from stud")
rows=cur.fetchall()
text=t.Text(root)
text.pack()
for row in rows:
    text.insert(t.END,str(row)+"\n")
con.commit()
cur.close()
con.close()

root.geometry("700x700")
root.mainloop()