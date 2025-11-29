import sqlite3 as sq
connn=sq.connect("MY.db")
cursor=connn.cursor()
cursor.execute("create table if not exists stud (rollno integer primary key autoincrement,name text,city text)")
cursor.close()
connn.close()
def insert():
    connn=sq.connect("MY.db")
    cursor=connn.cursor()
    cursor.execute("insert into stud(name,city)values(?,?)",("meet","keshod"))
    connn.commit()
    cursor.close()
    connn.close()
insert()