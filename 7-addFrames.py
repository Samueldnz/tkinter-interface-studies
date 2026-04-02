from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Adding Frames")
root.iconbitmap('logo.ico')

# frame is a little box with a label or not, its use to keep your organazed, just like section in HTML

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50) # this pad put space inside the frame

#if I dont wanna have a label in my frame, a just need to erase the texto from the builder
frame.pack(padx=10, pady=10) # puts pad/space between the frame border and the screem

b = Button(frame, text="Don´t Click Here!")
b2 = Button(frame, text="...or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()