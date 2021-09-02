from tkinter import *
from PIL import ImageTk, Image
import os

# create the list of images to display
current_img = 0
image_list = []
length = '0'

def create_image_list():
    global length
    for entry in os.scandir("./images"):
        image_list.append(
            ImageTk.PhotoImage(Image.open("images/"+entry.name).resize((500,500)))
        )

    length = str(len(image_list))

def load_first_image():
    global main_label

    main_label.grid_forget()
    main_label = Label(root, image=image_list[current_img])
    main_label.grid(row = 0, column = 0, columnspan = 3)

def initial_status():
    status = Label(root, text="image 1 of "+str(length), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root = Tk()
root.title("image viewer application")
root.iconbitmap("favicon.ico")

main_label = Label(root, image = None, text = "loading")
main_label.grid(row = 0, column = 0, columnspan = 3)

def forward():
    global main_label
    global current_img
    global status

    current_img+=1

    if current_img == len(image_list):
        current_img=0

    main_label.grid_forget()
    main_label = Label(root, image=image_list[current_img])
    main_label.grid(row = 0, column = 0, columnspan = 3)

    status = Label(root, text="image "+ str(current_img+1) +" of "+ length, bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back():
    global main_label
    global current_img
    global status

    current_img-=1

    if current_img < 0:
        current_img=len(image_list)-1

    main_label.grid_forget()
    main_label = Label(root, image=image_list[current_img])
    main_label.grid(row = 0, column = 0, columnspan = 3)
    
    status = Label(root, text="image "+ str(current_img+1) +" of "+ length, bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

status = Label(root, text="image 0 of "+ str(length), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="exit", command=root.quit)
button_forward = Button(root, text=">>", command = forward)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=3)

if __name__ == "__main__":
    create_image_list()
    load_first_image()
    initial_status()
    root.mainloop()