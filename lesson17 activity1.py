from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('image')
root.geometry('400x400')

upload = Image.open(r"C:\Users\Alek\Desktop\New folder\Alek Main\Python Course\Lesson 1\Childhood.jpeg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width=350)
label.place(x=50, y=50)
label12 = Label(root, text="this is how you add image in Tkinter Window")
label12.place(x=40, y=360)

root.mainloop()


