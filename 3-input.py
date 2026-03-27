from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ") # put some default text inside the input box

# and like the button, its possible to change the size, change the color and a lot of other parameter that can be used to modify the entry

def myClick():
    hello = "Hello " + e.get() # variable fields
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick)

# e.get() its used to get whatever is inside the input

myButton.pack()

root.mainloop()