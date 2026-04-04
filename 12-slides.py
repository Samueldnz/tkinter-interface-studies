from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Slides")
root.iconbitmap('logo.ico')
root.geometry("400x400") #the whole screen gets bigger to 400x400 size

# slides are not slides from powerpoint for example. Slides are slides bar, pretty similat to that one on the right in web page that is use to scroll the page

def slide():
    my_label = Label(root, text=horizontal.get())
    my_label.pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


vertical = Scale(root, from_=0, to=400) # specify where to start and where to finish
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

# the slides return a number based where they are

my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()