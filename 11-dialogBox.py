from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.title("Dialog Box")
root.iconbitmap('logo.ico')

# sometimes you wanna open a file, like pdf, doc or even a imagem. In order to accomplish this, you need to use something called file dialog

def open():
    global my_img
    base_dir = os.path.dirname(os.path.abspath(__file__))
    initialdir = os.path.join(base_dir, "imagesApp")

    # just returne the name and location of the file
    root.filename = filedialog.askopenfilename(initialdir=initialdir, title="Select A File", filetypes=(
        ("Image files", "*.png"),
        ("All files", "*.*")

    )) # first the diretory to started, it can be whateevr you want
    # title of the box
    # you can put to show all the files, or you can specify wich type of files do you wanna
    # to show all kind of files, just type "*.*" - seems like a face

    # if it has the filter to png in first place, the program will filter just for png So if in the folder doesn´t have any png images, it wont show anything even if it has other kind of documents

    # in order to fix this, we have to change the order and make the all files first or use the filter in the documents windows that will show. You can see this part in the bottom-right corner

    my_label = Label(root, text=root.filename)# will return the location, the path
    my_label.pack()

    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(image=my_img)
    my_img_label.pack()

my_btn = Button(root, text="Open File", command=open)
my_btn.pack()

root.mainloop()