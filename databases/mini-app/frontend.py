'''
This desktop application stored information about books
title, author
year, ISBN

user can:
view all records
search entry
add entry
update entry
delete
close
'''

from tkinter import *
from backend import * # custom py file

db = database_manager()

def get_selected_row(event):
    try:
        global selected_tuple
        index = book_list.curselection()[0]
        selected_tuple = book_list.get(index)

        # putting the selected row information in the entries
        entry_title.delete(0, END)
        entry_title.insert(END, selected_tuple[1])

        entry_author.delete(0, END)
        entry_author.insert(END, selected_tuple[2])
        
        entry_year.delete(0, END)
        entry_year.insert(END, selected_tuple[3])
        
        entry_ISBN.delete(0, END)
        entry_ISBN.insert(END, selected_tuple[4])
    except:
        pass

def delete_command():
    db.delete(selected_tuple[0])


def view_command():
    book_list.delete(0, END)
    for i, row in enumerate(db.view()):
        book_list.insert(i, row) # note: with row[1:] we dont' output the id

def search_command():
    book_list.delete(0, END)
    # print(type(entry_title.get()))
    # print(db.search(title = entry_title.get()))
    for i, row in enumerate(db.search(title = entry_title.get(),
                                      author = entry_author.get(),
                                      year = entry_year.get(),
                                      isbn = entry_ISBN.get() ) ):
        book_list.insert(i, row)
    
def add_command():
    db.insert(title = entry_title.get(),
              author = entry_author.get(),
              year = entry_year.get(),
              isbn = entry_ISBN.get())

def update_command():
    db.update(id = selected_tuple[0],
              title = entry_title.get(),
              author = entry_author.get(),
              year = entry_year.get(),
              isbn = entry_ISBN.get())
            
def close_program_command():
    db.close()
    window.destroy()

# GUI
window = Tk()

window.wm_title("book store")

# start entry widget
entry_title = Entry(window, width = 15)
entry_title.grid(row = 0, column = 0)
label_title = Label(window, text = "title")
label_title.grid(row = 0, column = 1)

entry_author = Entry(window, width = 15)
entry_author.grid(row = 0, column =2)
label_author = Label(window, text = "author")
label_author.grid(row = 0, column = 3)

entry_year = Entry(window, width = 15)
entry_year.grid(row = 1, column = 0)
label_year = Label(window, text = "year")
label_year.grid(row = 1, column = 1)

entry_ISBN = Entry(window, width = 15)
entry_ISBN.grid(row = 1, column = 2)
label_ISBN = Label(window, text = "ISBN")
label_ISBN.grid(row = 1, column = 3)
# end entry widget

# begin book list widget
book_list = Listbox(window, height = 5, width = 36)
book_list.grid(row = 2, rowspan = 6, column = 0, columnspan = 2)
book_list_scrollbar = Scrollbar(window)
book_list_scrollbar.grid(row = 3, column = 2)
book_list_scrollbar.config(command = book_list.yview)
book_list.config(yscrollcommand = book_list_scrollbar.set)

book_list.bind("<<ListboxSelect>>", get_selected_row)

# end book list widget

view_all_button = Button(window, text = "view all", command = view_command)
view_all_button.grid(row = 3, column = 3)

search_entry_button = Button(window, text = "search entry", command = search_command)
search_entry_button.grid(row = 4, column = 3)

add_entry_button = Button(window, text = "add entry", command = add_command)
add_entry_button.grid(row = 5, column = 3)

update_button = Button(window, text = "update", command = update_command)
update_button.grid(row = 6, column = 3)

delete_button = Button(window, text = "delete", command = delete_command)
delete_button.grid(row = 7, column = 3)

close_button = Button(window, text = "close", command = close_program_command)
close_button.grid(row = 8, column = 3)

window.mainloop()
db.close()

def f():
    top = Toplevel()
    label = Label(top, text="I exists :)").pack()
 
btn = Button(DataEntry, text="click me", command=f).grid(row=8, column=0)