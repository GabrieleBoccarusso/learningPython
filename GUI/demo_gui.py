from tkinter import *

# behavior

def km_to_miles():
    miles = float(e1_value.get())*1.6
    miles = round(miles, 2)
    t1.insert(END, miles)

# GUI
window = Tk()

b1 = Button(master = window, text = "km to miles", command = km_to_miles)
b1.grid(row = 0, column = 0)

b2 = Button(master = window, text = "nothig")
b2.grid(row = 0, column = 1)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 2, columnspan = 2, column = 0)

t1 = Text(window, height = 1, width = 15)
t1.grid(row = 3, column = 0, columnspan = 2)

window.mainloop()
