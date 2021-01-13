import sqlite3
from sqlite3 import Error


def connect(database):
    conn = None
    try:
        conn = sqlite3.connect(database, check_same_thread=False)
    except Error as e:
        print(e)
    return conn


class SQLibrary:
    def __init__(self):
        self.conn = connect("library.db")
        self.allitems = {}
        self.c = self.conn.cursor()

    def all(self):
        try:
            self.c.execute("SELECT * FROM books")
            self.allitems = self.c.fetchall()
        except Error as e:
            print(e)
        return self.allitems

    def get(self, book_id):
        try:
            result = self.c.execute(f"SELECT * FROM books WHERE id = {book_id}")
        except Error as e:
            print(e)
        else:
            return result

    def create(self, data):
        try:
            new_data = []
            for item in data:
                new_data.append(data[item])
            self.c.execute(
                f"INSERT INTO books (title, author, pages, description, price) VALUES(?,?,?,?,?)", tuple(new_data[:5]))
        except Error as e:
            print(e)

    def update(self, book_id, data):
        query = []
        for item in data:
            query.append(f"{item} = '{data[item]}'")
        q = ", ".join(query[:5])
        try:
            self.c.execute(f"UPDATE books SET {q} WHERE id = {book_id}")
        except Error as e:
            print(e)

    def save_all(self):
        try:
            self.conn.commit()
        except Error as e:
            print(e)

    def delete(self, book_id):
        try:
            self.c.execute(f"DELETE FROM books WHERE id = {book_id}")
        except Error as e:
            print(e)


bookstore = SQLibrary()
