from tkinter import *

root = Tk()

# build a function to execute when the button get clicked
def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

    # when you click in the button, it prints in the scree the text inside the function. IF you click again, it will print again over and over again

myButton = Button(root, text="Click me!", command=myClick, fg="blue", bg="red")

# if you put a () in the fucntion inside Button(), you gonna call the function just one time, before it prints the button and the code wont works as supposed to work

# you can disable the button just adding a state in it. After text, just add state=DISABLED. Button(root, text="Click me!", state=DISABLED)

# or change the size using "padx = ?", making wider or longer using "pady = ?"

# fg makes the text change the color, you can use bg for background. Can be used as hexadecimal code color or the color`s name`
myButton.pack()

root.mainloop()