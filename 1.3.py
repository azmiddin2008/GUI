# Button tkinter - button chiqarish
from tkinter import *

root = Tk()
def click():
    label=Label(root,text="Bu")
    label.pack()
def submit():
    label=Label(root,text="u")
    label.pack()
button = Button(root, text="bosing", command=click, fg="white",bg="black",border="8px solid green",)
buttonn = Button(root, text="bosing", command=submit, fg="white",bg="black",border="8px solid green",)


button.pack()
buttonn.pack()







root.mainloop()

