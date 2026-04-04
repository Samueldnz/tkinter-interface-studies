from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Basic Window")
root.iconbitmap('logo.ico')

def open():
    global my_img
    top = Toplevel() # in a code with just this line inside, when it runs, it shows two windows, the default one and a second one
    top.title('Second Window')
    top.iconbitmap('logo.ico')

    my_img = ImageTk.PhotoImage(Image.open("imagesApp/muzan.jpg")) # it needs to be a global variable because for some reason when you are in a function like this to a second window, python sees this local variable and thinks like garbage
    my_label = Label(top, image=my_img)
    my_label.pack()

    btn2 = Button(top, text="Close window", command=top.destroy)
    btn2.pack()

btn = Button(root, text="Open Second Windo", command=open)
btn.pack()

root.mainloop()