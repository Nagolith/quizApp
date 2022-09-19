# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to Quiz making App")

# Set geometry(width x height)
root.geometry('1000x800')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
item.add_command(label='Close')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the root window
lbl = Label(root, text = "How many quiz questions would you like to make?")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)

# function to display text when
# button is clicked
def clicked():
    #res = "You wrote " + txt.get()
    #lbl.configure(text = res)
    iterations = int(txt.get())
    for i in range (iterations):
        lbl = Label(root, text = "Question number ")
        lbl.grid()


# button widget with red color text
# inside
btn = Button(root, text = " Generate lines" ,
             fg = "red", command = clicked)



# iterating over quiz questions


# set Button grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.mainloop()
