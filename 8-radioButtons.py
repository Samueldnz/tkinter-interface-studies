from tkinter import *

root = Tk()
root.title("Radio Buttons")
root.iconbitmap("logo.ico")

# r = IntVar() # we are using this type of variable in order to be able to use some function inside IntVar. It can be other types, like string using StrVar
# r.set("2")

# supose a pizza menu
MODES = [
    ("Pepperoni", "Pepperoni"), # text, value/mode
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni") #set first one to be marked on screen

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack() # assigned a variable to get when the radion is clicked in order to use the value in other things

# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 3", variable=r, value=3, command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()