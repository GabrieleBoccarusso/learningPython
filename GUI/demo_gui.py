from tkinter import *

window = Tk()

b1 = Button(master = window, text = "first")
b1.grid(row = 0, column = 0)
b2 = Button(master = window, text = "second")
b2.grid(row = 0, column = 1)
e1 = Entry()
e1.grid(row = 2, columnspan = 2, column = 0)
t1 = Text(window, height = 1, width = 15)
t1.grid(row = 3, column = 0, columnspan = 2)

window.mainloop()
