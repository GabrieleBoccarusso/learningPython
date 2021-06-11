import sqlite3

class database_manager():
    def __init__(self):
        self.connector = sqlite3.connect("data/database_file.db")
        self.cursor = self.connector.cursor()

        # create the table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Books (
                                                        id INTEGER PRIMARY KEY, 
                                                        title TEXT,
                                                        author TEXT,
                                                        year INTEGER,
                                                        isbn INTEGER)""")
        self.connector.commit()

    def insert(self, title, author, year, isbn):
        self.cursor.execute(f"""INSERT INTO Books VALUES (
            NULL, ?, ?, ?, ?)""", 
            (title, author, year, isbn))
        self.connector.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM Books")
        return self.cursor.fetchall()


db = database_manager()
db.insert("a", "juan", 0, 5232)