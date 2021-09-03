'''
introduction in python to databases,
this way makes to code more efficient that always opening and
closing the connection.
Ideally in a real program there would be an object
with different tables and with the ID column in every one of them,
but this is just an example
Gabriele Boccarusso 2021.06.10 - yyyy.mm.dd
'''

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

    return conn, cur

def insert(conn, cur, item, quantity, price): 
    cur.execute(f"INSERT INTO Store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()

def view(cur):
    cur.execute("SELECT * FROM Store")
    return cur.fetchall()

def delete(conn, cur, item):
    cur.execute("DELETE FROM Store WHERE item = ?", (item,))
    conn.commit()

def update(conn, cur, item, quantity, price):
    cur.execute("UPDATE Store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    conn.commit()

def main():
    conn, cur = create_table()

    print("1: insert\n2: delete\n3: view\n4: update")

    action = int(input(':'))

    if action == 1:
        item = input("enter item name: ")
        quantity = input("enter quantity: ")
        price = input("enter price: ")
        insert(conn, cur, item, quantity, price)
    elif action == 2:
        item = input("enter item name: ")
        delete(conn, cur, item)
    elif action == 3:
        print(view(cur))
    elif action == 4:
        item = input("enter item name: ")
        quantity = input("enter new quantity: ")
        price = input("enter  new price: ")
        update(conn, cur, item, quantity, price)


    conn.close()

main()