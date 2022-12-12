from tkinter import *
root= Tk()
def myClick():
    myLabel = Label(root, text="clicked")
    myLabel.pack()
def myClick2():
    myLabel1 = Label(root, text="clicked button2")
    myLabel1.pack()
myButton= Button(root, text="press here", padx=50, pady=50,command=myClick)
myButton2= Button(root, text="button2", padx=50, pady=50,command=myClick2)
myButton.pack()
myButton2.pack()
root.mainloop()