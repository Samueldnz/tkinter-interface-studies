from tkinter import *
from PIL import ImageTk, Image

root = Tk() 

# there is a problem with the invert bars, so to fix that, use double invert bars

root.title('Icons, Images and Exit Buttons')
root.iconbitmap('logo.ico')

# root has some image that support two types, mostly GIF, and to use other kind of imagens like PNG, JPEG we need to import

my_img = ImageTk.PhotoImage(Image.open("pantera.jpeg")) # creating image
my_label = Label(image=my_img)
my_label.pack()

# for this exercise, choose small pictures, is better to position, I used on in 300x300


button_quit = Button(root, text="Exit Program", command=root.quit) # inside root there is a function called quit
button_quit.pack()


root.mainloop()