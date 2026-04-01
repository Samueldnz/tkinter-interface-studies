from tkinter import *
from PIL import ImageTk, Image

root = Tk() 
root.title("Image Viewer App")

my_img1 = ImageTk.PhotoImage(Image.open("imagesApp/L.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("imagesApp/lulamolusco.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("imagesApp/muzan.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("imagesApp/patrick.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("imagesApp/veget.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("imagesApp/zoro.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6] # simple list

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3) # columnspan is about how long the thing will be. For exmaple, in this case, the imagem is in column 0 but expand until column 2

def forward(image_number):
    global my_label
    global vforward
    global vback

    my_label.grid_forget() # makes the grid disapear
    my_label = Label(image=image_list[image_number-1]) # since we are passing 2 and the index in the list starts at 0, we need to decrease in 1 value
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    # disable if the list finished
    if image_number == 6:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global vforward
    global vback

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1]) 

    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    # disable if the list finished
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# there somekind of direction system, like north and south. We can strech using sticky
root.mainloop()