from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("database application")
root.geometry("400x400")

# create a database or connect to one
# conn stands for connector
conn = sqlite3.connect("address_book.db")
# cur stands for cursor
cur = conn.cursor()

# create table
cur.execute("""CREATE TABLE IF NOT EXISTS addresses (
		first_name text,
		last_name text,
		zipcode integer
		)""")

# create delete record function for db
def delete():
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()

    cur.execute("DELETE from addresses where oid = " + DeleteEntry.get())

    DeleteEntry.delete(0, "end")
    conn.commit()
    conn.close()

# create submit function for db
def submit():
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO addresses VALUES (?, ?, ?)",
                (
                    FirstNameEntry.get(),
                    LastNameEntry.get(),
                    ZipcodeEntry.get()
                ))

    conn.commit()
    conn.close()
    # clear text box
    FirstNameEntry.delete(0, END)
    LastNameEntry.delete(0, "end")
    ZipcodeEntry.delete(0, "end")

# create query function for db
def query():
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()

    cur.execute("SELECT *, oid FROM addresses")
    # cur.fetchone() # fetch the first
    # cur.fetchmany(10) # fetch the first ten
    records = cur.fetchall()
    # print(records)

    print_records = ''
    for record in records:
        print(record)
        print_records += str(record[3]) + ' ' + str(record[1]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()

# create entries and labels
FirstNameLabel = Label(root, text = "first name")
FirstNameLabel.grid(row=0, column=0)
FirstNameEntry = Entry(root, width=30)
FirstNameEntry.grid(row=0, column=1, padx=20)

LastNameLabel = Label(root, text = "last name")
LastNameLabel.grid(row=1, column=0)
LastNameEntry = Entry(root, width=30)
LastNameEntry.grid(row=1, column=1, padx=20)

ZipcodeLabel = Label(root, text = "zipcode name")
ZipcodeLabel.grid(row=2, column=0)
ZipcodeEntry = Entry(root, width=30)
ZipcodeEntry.grid(row=2, column=1, padx=20)

DeleteLabel = Label(root, text="delete ID number")
DeleteLabel.grid(row=5, column=0)
DeleteEntry = Entry(root, width=30)
DeleteEntry.grid(row=5, column=1)

# create submit button
SubmitBtn = Button(root, text="add record to database", command=submit)
SubmitBtn.grid(row=4, column=0, columnspan=2)

# create query button
QueryBtn = Button(root, text="show records", command=query)
QueryBtn.grid(row=3, column=0, columnspan=2)

# create delete button
DeleteBtn = Button(root, text="delete records", command=delete)
DeleteBtn.grid(row=7, column=0, columnspan=2)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()