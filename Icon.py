from tkinter import *
root= Tk()
root.title("img and icon input")
root.iconbitmap("C:/Users/yashs/Desktop/iconn.ico")
quit_button = Button(root, text="QUIT", command=root.quit)
quit_button.pack()

root.mainloop()