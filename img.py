from tkinter import *
from PIL import Image,ImageTk
root= Tk()
root.title("img input")
root.iconbitmap("C:/Users/yashs/Desktop/iconn.ico")
my_img = ImageTk.PhotoImage(Image.open("C:/Users/yashs/Desktop/download.jpeg"))
my_label = Label(image=my_img)
my_label.pack

root.mainloop()