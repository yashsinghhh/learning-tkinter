from tkinter import *
root= Tk()

e=Entry(root,borderwidth=3)
e.pack()
e.get()
e.insert(0, 'Enter your name')


def myClick():
    myLabel = Label(root, text="clicked "+e.get())
    myLabel.pack()
    
myButton= Button(root, text="press here", padx=50, pady=50,command=myClick)

myButton.pack()
root.mainloop()