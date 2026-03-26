from tkinter import *

# a better way to position things on the screen
# grid with columns and rows starting with 0

root = Tk();

myLabel1 = Label(root, text="Hello Word!") 
myLabel2 = Label(root, text="My Name Is Samuel") 
myLabel3 = Label(root, text="            ")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)
 

root.mainloop()

# although we resized the window, the text won`t resized too, since we fixed the rows and column.`

# even if we use a column = 5, if doesn´t have anything in the column 1, 2, 3 and 4, the program will just ignore. So the output will be the same as column=1

# if we wanna somenthing between the texts, we gonna need ghost texts as myLabel3

# you can put everything together like: myLabel1 = Label(root, text="Hello Word!").grid(row=0, column=0)