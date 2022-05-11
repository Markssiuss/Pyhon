
import sqlite3 as sq3

class Database:

    def __init__(self, db):
        self.conn = sq3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookstore (Id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, Isbn INTEGER)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM bookstore")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM bookstore WHERE Title=? OR Author=? OR Year=? OR Isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM bookstore WHERE Id=?", (id,))
        self.conn.commit()

    def update(self, id,title, author, year, isbn):
        self.cur.execute("UPDATE bookstore SET Title=? , Author=? , Year=? , Isbn=? WHERE Id=?", (title, author, year, isbn, id))
        self.conn.commit()
