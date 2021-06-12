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

    def search(self, title = '', author = '', year = '', isbn = ''):
        self.cursor.execute("SELECT * FROM Books WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        return self.cursor.fetchall()
    
    def delete(self, id):
        self.cursor.execute("DELETE FROM Books WHERE id = ?", (id,))
        self.connector.commit()
    
    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE Books SET title = ?, author = ?, year = ?, isbn = ?", (title, author, year, isbn, id))
        self.connector.commit()

    def close(self):
        self.connector.close() # closing the connection to the server
                               # before destroying the class