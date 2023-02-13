from tkinter import *
from tkinter import filedialog  
from tkinter import messagebox
from PIL import ImageTk,Image

root =Tk()
def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir = 'images',title ='rasmni tanlang',
    filetypes =(('jpg files','*.jpg'),('all files','*.*')))
    img = ImageTk.PhotoImage(Image.open(root.filename))
    Label( image=img).pack()



    # info=
    # messagebox.askyesno('Installation','Siz rasmni qoymoqchimisiz')
    # Label(root,text=info).pack()

      

Button(root,text="Rasm kerak bolsa bosing",command=open,bg="green",fg='white').pack()








mainloop()