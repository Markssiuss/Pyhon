
import sqlite3 as sq3
def create():
    conn = sq3.connect("TkinterGUI\\books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore (Id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, Isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sq3.connect("TkinterGUI\\books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sq3.connect("TkinterGUI\\books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sq3.connect("TkinterGUI\\books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookstore WHERE Title=? OR Author=? OR Year=? OR Isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sq3.connect("TkinterGUI\\books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE Id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title, author, year, isbn):
    conn = sq3.connect("TkinterGUI\\books.db")
    cur = conn.cursor()
    cur.execute("UPDATE bookstore SET Title=? , Author=? , Year=? , Isbn=? WHERE Id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()
