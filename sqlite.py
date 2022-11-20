import sqlite3

def createTable():
  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quant INTEGER, price REAL)")
  conn.commit()
  conn.close()

def insert(item,quant,price):
  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quant,price))
  conn.commit()
  conn.close()

def view():
  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM store")
  rows=cur.fetchall()
  conn.close()
  return rows

def delete(item):
  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("DELETE FROM store WHERE item=?",(item,))
  conn.commit()
  conn.close()

def update(quant, item):
  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("UPDATE store SET quant=? WHERE item=?",(quant,item))
  conn.commit()
  conn.close()

createTable()
insert("browar",1,2)
#delete("browar")
update(2,"browar")
print(view())
