from Tkinter import *

root = Tk()

label = Label(root,text="Welcome to Python")

canvas = Canvas(root,bg="white")

button = Button(root,text="Click me")

label.pack()
canvas.pack()
button.pack()

root.mainloop()


