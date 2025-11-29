from tkinter import *
root=Tk()
root.geometry("500x500")

li=Listbox(root)
li.place(x=20,y=30)

li.insert(END,"anb")

li.insert(END,"anb")

li.insert(END,"anb")

li.insert(END,"anb")

li.insert(END,"anb")

li.insert(END,"anb")

lb1=Label(root,text="?")
lb1.place(x=20,y=200)


def getdata():

    selectd=li.curselection()
    value=li.get(selectd[0])
    lb1.config(text=value)

btn1=Button(root,text="get",command=getdata)
btn1.place(x=20,y=220)
root.mainloop()