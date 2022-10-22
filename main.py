# Import Module
from tkinter import *

# create root window
root = Tk()

# variables
answer = ""
answer_entry = Entry()
correct_answer = ""
num = 0
question = ""
quest_var = {"":""}
quest_label = Label()
quest_entry = Entry()


# root window title and dimension
root.title("Welcome to Quiz making App")

# Set geometry(width x height)
root.geometry('1000x800')


def generate(num, question, answer, var_quest):
    for num in range(num):
        quest_label = Label(root, text = "Question:", font = ("calibre", 12))
        quest_entry = Entry(root, textvariable = question, font = ("calibre", 12))
        var_quest = {question:""}

    for question in range(num):
        answer_entry = Entry(root, textvariable = answer, font = ("calibre", 12), show = "*")
        var_quest = {question:answer}

    return var_quest



     

def submit(j, num):
    for j in range (num):
        question = j.get()

    for j in range (num):
        print("Question is: " + question)

    for j in range (num):
        j.set("")



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

# button for input and output text
display = Button(root, height = 2,
                width = 20, text = "Show"
                ,command = lambda:get_input())

generate_label = Label(root, text = "How many quiz questions would you like to make?", font = ("calibre", 12))
generate_entry = Entry(root, textvariable = num, font = ("calibre", 12))

quest_var = generate(num, question, answer, quest_var)
gen_btn = Button(root, text = "Generate", command = generate(num, question, answer, quest_var), )
sub_btn = Button(root, text = "Submit", command = submit(quest_var, num))

generate_label.grid(row = 0, column = 0)
generate_entry.grid(row = 0, column = 1)
quest_label.grid(row = 1, column = 0)
quest_entry.grid(row = 1, column = 1)
answer_entry.grid(row = 1, column = 2)
gen_btn.grid(row = 0, column = 2)
sub_btn.grid(row = 2, column = 1)

# Execute Tkinter
root.config(menu=menubar)
root.mainloop()
