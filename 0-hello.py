from tkinter import *

# everything is a widget, the first one you need to create is a bigger one

root = Tk(); # before anyone else

# to create anythig, you need to use 2 steps. You have to efine the thing and then put it on the screen

myLabel = Label(root, text="Hello Word!") 

# create

# now we need to put it on the screen. Just packing, you are just shoving it in there at the first available spot. A very base way to do this

myLabel.pack()

# last thung: loop event

root.mainloop()
