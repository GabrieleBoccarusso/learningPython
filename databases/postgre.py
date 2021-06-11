'''
notes
1:  to prevent sequele injections is better to pass an element directly,
    but this way we have an error, that's why to pass a string into the SQWL table
    we have to put around the string "'" to ge the effect 'item'
'''

import psycopg2

def justify(string): # see 1
    return "'" + string + "'"

def create_table():
    conn = psycopg2.connect("dbname='PyDatabase' user='postgres' password='root' host='localhost' port='5432'")
    cur = conn.cursor()

    # execute the query
    cur.execute("CREATE TABLE IF NOT EXISTS Store (item TEXT, quantity INTEGER, price REAL)")

    # commit the changes
    conn.commit()

    return conn, cur

def insert(conn, cur, item, quantity, price): 
    # cur.execute(f"INSERT INTO Store VALUES (?,?,?)", (item, quantity, price))
    # cur.execute("INSERT INTO Store VALUES (%s,%s,%s)" % (item,quantity,price))
    cur.execute(f"INSERT INTO Store VALUES ({justify(item)},{quantity},{price})")
    conn.commit()

def view(cur):
    cur.execute("SELECT * FROM Store")
    return cur.fetchall()

def delete(conn, cur, item):
    cur.execute(f"DELETE FROM Store WHERE item = {justify(item)}")
    conn.commit()

def update(conn, cur, item, quantity, price):
    cur.execute(f"UPDATE Store SET quantity = {justify(item)}, price = {price} WHERE item = {item}")
    conn.commit()

def main():
    conn, cur = create_table()
    loop = 'y'
    while(loop[0] == 'y'):
        print("1: insert\n2: delete\n3: view\n4: update")

        action = int(input('enter action:'))

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
        
        loop = input("Do you want to continue? ")


    conn.close()

main()