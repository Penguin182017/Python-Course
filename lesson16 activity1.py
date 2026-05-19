from tkinter import *

window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

greeting = Label(text="Hello, User", fg='black', bg='white')
button = Button(text='Click Me', fg='white', bg='blue')
entry = Entry(fg='yellow', bg='blue')
greeting.pack()
button.pack()  
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text="Sample Frame")
label.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()
window.mainloop()