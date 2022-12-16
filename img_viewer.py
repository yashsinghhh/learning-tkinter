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
def forward(img_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=img_list[img_num-1])
    button_forward = Button(root, text="forward", command=lambda: forward(img_num+1))
    button_back = Button(root, text="back", command=lambda: back(img_num-1))
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    if img_num == 5:
        button_forward = Button(root,text="",state=DISABLED)
def back(img_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=img_list[img_num-1])
    button_forward = Button(root, text="forward", command=lambda: forward(img_num+1))
    button_back = Button(root, text="back", command=lambda: back(img_num-1))
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
button_back = Button(root, text="back", command=lambda: back())
button_quit = Button(root, text="Quit",command=root.quit)
button_forward = Button(root, text="forward", command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()