import sqlite3 as sq
connn=sq.connect("mydb2323")
cursor=connn.cursor()
cursor.execute("create table if not exists stud (rollno integer primary key autoincrement,name text,city text)")
cursor.close()
connn.close()   