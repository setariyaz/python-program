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
