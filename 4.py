# images --------- image
from tkinter import *
from PIL import ImageTk,Image

root =Tk()
root.title("Images ")

image =ImageTk.PhotoImage(Image.open("images/rasm.jpeg"))

img =Label(root, image=image)
img.pack(padx=10,pady=10, )




















root.mainloop()