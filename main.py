# Import Module
from tkinter import *

# create root window
root = Tk()

# variables
correct_answer = ""


# root window title and dimension
root.title("Welcome to Quiz making App")

# Set geometry(width x height)
root.geometry('1000x800')

# function to iterate text when
# button is clicked
def clicked():
    iterations = int(txt.get())
    for i in range (iterations):
        num = i + 1
        lbl = Label(root, text = "Question number " + str(num))
        lbl.grid()

# set background to dark mode
def dark_mode():
    root['bg'] = 'black'

# set background to light mode
def light_mode():
    root['bg'] = 'white'

# take input for question and evaluate
# if true of false
def get_input():
    INPUT = inputtxt.get("T","F")
    print(INPUT)
    if(INPUT == correct_answer):
        output.insert(END, "Correct!")
    else:
        output.insert(END, "Wrong answer")

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menubar = Menu(root)
item = Menu(menubar, tearoff = 0)
menubar.add_cascade(label='File', menu = item)
item.add_command(label='New', command = None)
item.add_command(label='Light mode', command = light_mode)
item.add_command(label='Dark mode', command = dark_mode)
item.add_separator()
item.add_command(label='Close', command = root.destroy)

inputtxt = Text(root, height = 10, width = 25
                ,bg = "light yellow")

output = Text(root, height = 5, width = 25
            ,bg = "light cyan")

# adding a label to the root window
lbl = Label(root, text = "How many quiz questions would you like to make?")
lbl.grid()

# adding Entry Field
txt = Entry(root, width = 10)
txt.grid(column = 1, row = 0)

# button widget with red color text
# inside
btn = Button(root, text = " Generate lines" ,
             fg = "red", command = clicked)

# button for input and output text
display = Button(root, height = 2,
                width = 20, text = "Show"
                ,command = lambda:get_input())


# set Button grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.config(menu=menubar)
root.mainloop()
