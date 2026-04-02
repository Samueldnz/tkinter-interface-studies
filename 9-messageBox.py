from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.iconbitmap('logo.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello Word") # the first text is the box name, and the second one is the content inside this box
    
    #askyesno, askokcancel
    if response == 1:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()

Button(root, text="Popup", command=popup).pack()


root.mainloop()