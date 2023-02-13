from tkinter import *
from tkinter import messagebox
root = Tk()

# Showinfo,Showerror,Showwarnig
# askyesno,askokcancel,askyesnocancel,askquestion,askretrycancel

def click():
    info=   messagebox.askyesno('Installation','Siz hozir hozir oyin oynaysizmi')
    Label(root,text=info).pack()
    if info ==1:
        Label(root,text='Siz oyinga kirdingiz').pack()
    elif info==0:
        Label(root,text='siz oyinga kirmadingiz').pack()
        

Button(root,text="Message",command=click,bg="green",fg='white').pack()


























root.mainloop()