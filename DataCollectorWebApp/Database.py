from itertools import count
import sqlite3 as sq3

class Database:

    def __init__(self, db):
        self.conn = sq3.connect(db, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS heightsurvey (Id INTEGER PRIMARY KEY, Email TEXT, Height INTEGER)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def insert(self, Email, Height):
        self.cur.execute("INSERT INTO heightsurvey VALUES (NULL, ?, ?)", (Email, Height))
        self.conn.commit()

    def checkUniqueEmail(self, Email):
        self.cur.execute("SELECT * FROM heightsurvey WHERE Email=?", (Email, ))
        rows = self.cur.fetchall()
        return not (len(rows) > 0)