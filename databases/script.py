import sqlite3

def create_table():
    # create a connection with the database
    conn = sqlite3.connect("data/lite.db")

    # create the cursor to interact with the database
    cur = conn.cursor()

    # execute the query
    cur.execute("CREATE TABLE IF NOT EXISTS Store (item TEXT, quantity INTEGER, price REAL)")

    # commit the changes
    conn.commit()

    # close the connection
    conn.close()

def insert(item, quantity, price): 
    conn = sqlite3.connect("data/lite.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("data/lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store")
    rows = cur.fetchall()
    conn.close()
    return rows

create_table()

insert("Cup", 50, 1.1)

print(view())

# note: there is a better way than establishing a connection and creating a cursor every time?