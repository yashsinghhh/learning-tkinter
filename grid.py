from tkinter import *
root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is xyz")
# shoving onto the screen 
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)#columns are relative so if column is 5 or 1 or 2 itll be at the same so we 
# have to add space labels for right spacing 
root.mainloop()
