from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root = Tk()

img_frame = LabelFrame(root,text="",padx=5,pady=5)
img_frame.pack(padx=10,pady=10)

def click():
    global info
    global img
    global img1
    info = messagebox.askyesno('Installation','Siz rasm kormoqchimisiz')
    # Label(root,text=info).pack()
    if info ==1:
            img = ImageTk.PhotoImage(Image.open("images/r.jpg"))
            Label(img_frame, image=img).pack()
    else:
        Label(root,text='sizga rasm yoq').pack()
        

Button(root,text="Message",command=click,bg="green",fg='white').pack()









root.mainloop()