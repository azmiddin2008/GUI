from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400')
var =StringVar()
chesk = Checkbutton(root,text='sizning shartlarizga roziman',offvalue='roziman',onvalue='rozimasman',variable=var)
chesk.pack()


def click():
    info=   messagebox.askyesno('Installation','chekboksni bosmoqchimisiz')
    Label(root,text=info).pack()
button = Button(root,text='click',command=click,bg='black',fg='white',padx=30,pady=10)
button.pack()
mainloop()