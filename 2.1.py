from tkinter import *
root = Tk()

frame =LabelFrame(root,text="",padx=200,pady=100,border="3px solid green",bg="red")
input = Entry(root, width=40,borderwidth=10)
input.insert(0, "ismingizni kiriting: ")

def click():
    label =Label(root,text=input.get)
    label.pack()
def delete():
    input.delete(0,END)
frame2 =LabelFrame(root,text="",padx=100,pady=50,border="3px solid green",bg="red")
button = Button(frame2, text='Bosing', command=click, padx=10,pady=5,fg="black",bg="yellow")

frame3 =LabelFrame(root,text="",padx=100,pady=50,border="3px solid green",bg="red")
button_delete =Button(frame3,text='Delete',command=delete,padx=10,pady=5,fg="black",bg="yellow")
input.grid(row=0,column=0)

frame2.grid(row=1,column=0)
button.pack()

frame3.grid(row=1, column=1)
button_delete.pack(padx=5,pady=5)

# frame.pack(padx=100,pady=100, )



# frame.pack(padx=200,pady=100, )


root.mainloop()