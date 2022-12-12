from tkinter import *
root= Tk()
def myClick():
    myLabel = Label(root, text="clicked")
    myLabel.pack()
myButton= Button(root, text="press here", padx=50, pady=50,command=myClick)
# , state=DISABLED is used in brackets to disable the button(unclickable)
myButton.pack()
root.mainloop()