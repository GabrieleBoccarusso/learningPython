'''
exercise:
Create a Python program that expects a kilogram input 
value and converts that value to grams, pounds, and ounces
when the user pushes the Convert button

Gabriele Boccarusso 2021.06.10 - yyyy.mm.dd
'''

from tkinter import *
from tkinter import messagebox



# behavior

def verify_input(num):
    res = False
    try: # we need a try because we'll always receive a string
        num = float(num)
        res = True
    except:
        # clear input section
        main_entry.delete(0, END)
        # send error message
        messagebox.showerror("Digitation error", 
                             "You entered and invalid input\nPlease enter a number")
    
    return res

def convertor():
    input = main_entry.get()

    if verify_input(input):
        input = float(input)
        # enable the writing into the text boxes
        grams_output.config(state = "normal")
        pounds_output.config(state = "normal")
        ounces_output.config(state = "normal")

        # delete everything was in the text boxes before
        grams_output.delete("1.0", "end")
        pounds_output.delete("1.0", "end")
        ounces_output.delete("1.0", "end")

        # insert output into the text boxes
        grams_output.insert(END, str(round(input *  1000, 3)))
        pounds_output.insert(END, str(round(input *  2.20462, 3)))
        ounces_output.insert(END, str(round(input *  35.274, 3)))

        # disable the text boxes again
        grams_output.config(state = "disabled")
        pounds_output.config(state = "disabled")
        ounces_output.config(state = "disabled")

    # end function

# GUI
# length of the various specifiers
spec_length = 9
window = Tk()

'''
interface outline:
entry activation_button
grams_output specifier
pounds_output specifier 
ounces_output specifier
'''
# main button
main_button = Button(window, text = "Convert", command = convertor)
main_button.grid(row = 0, column = 1)

# main input
main_entry = Entry(window)
main_entry.grid(row = 0, column = 0)

# grams output
grams_output = Text(window, height = 1, width = 15)
grams_output.config(state = "disabled")
grams_output.grid(row = 1, column = 0)

# grams specifier
grams_spec = Text(window, height = 1, width = spec_length)
grams_spec.grid(row = 1, column = 1)
grams_spec.insert(INSERT, "<- grams")
grams_spec.config(state = "disabled")

# pounds output
pounds_output = Text(window, height = 1, width = 15)
pounds_output.config(state = "disabled")
pounds_output.grid(row = 2, column = 0)

# pounds specifier
pounds_spec = Text(window, height = 1, width = spec_length)
pounds_spec.grid(row = 2, column = 1)
pounds_spec.insert(INSERT, "<- pounds")
pounds_spec.config(state = "disabled")

# ounces output
ounces_output = Text(window, height = 1, width = 15)
ounces_output.config(state = "disabled")
ounces_output.grid(row = 3, column = 0)

# ounces specifier
ounces_spec = Text(window, height = 1, width = spec_length)
ounces_spec.grid(row = 3, column = 1)
ounces_spec.insert(INSERT, "<- ounces")
ounces_spec.config(state = "disabled")

window.mainloop()