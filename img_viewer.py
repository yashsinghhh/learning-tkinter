from tkinter import *
from PIL import Image,ImageTk
root= Tk()
img1 = ImageTk.PhotoImage(Image.open("images/1.jpeg"))
img2 = ImageTk.PhotoImage(Image.open("images/2.jpeg"))
img3 = ImageTk.PhotoImage(Image.open("images/download.jpeg"))
img_list = [img1,img2,img3]

my_label = Label(image=img1)
my_label.grid(row=0,column=0,columnspan=3)
# my_label1 = Label(image=img2)
# my_label1.pack()
# my_label2 = Label(image=img3)
# my_label2.pack()

button_back = Button(root, text="back")
button_quit = Button(root, text="Quit",command=root.quit)
button_forward = Button(root, text="forward")

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=0)
button_forward.grid(row=1,column=0)

root.mainloop()