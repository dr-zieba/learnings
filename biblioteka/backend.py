import sqlite3

class Database:
    def __init__(self, db):
      self.conn=sqlite3.connect(db)
      self.cur=self.conn.cursor()
      self.cur.execute("CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY, titlE TEXT, author TEXT, year INTEGER, isbn INTEGER)")
      self.conn.commit()

    def add(self, title,author,year,isbn):
      self.cur.execute("INSERT INTO store VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
      self.conn.commit()

    def showAll(self):
      self.cur.execute("SELECT * FROM store")
      rows = self.cur.fetchall()
      return rows

    def search(self, title="",author="",year="",isbn=""):
      self.cur.execute("SELECT * FROM store WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
      rows = self.cur.fetchall()
      return rows

    def delete(self, id):
      self.cur.execute("DELETE FROM store WHERE id=?",(id,))
      self.conn.commit()

    def update(self,title,author,year,isbn,id):
      self.cur.execute("UPDATE store SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
      self.conn.commit()

    def __del__(self):
      self.conn.close()
