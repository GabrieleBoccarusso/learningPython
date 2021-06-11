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

# GUI
window = Tk()

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
book_list_scrollbar.grid(row = 3, column = 2, sticky = 'w')
book_list_scrollbar.config(command = book_list.yview)
book_list.config(yscrollcommand = book_list_scrollbar.set)
# end book list widget

view_all_button = Button(window, text = "view all")
view_all_button.grid(row = 3, column = 3)

search_entry_button = Button(window, text = "search entry")
search_entry_button.grid(row = 4, column = 3)

add_entry_button = Button(window, text = "add entry")
add_entry_button.grid(row = 5, column = 3)

update_button = Button(window, text = "update")
update_button.grid(row = 6, column = 3)

delete_button = Button(window, text = "delete")
delete_button.grid(row = 7, column = 3)

close_button = Button(window, text = "close")
close_button.grid(row = 8, column = 3)

window.mainloop()