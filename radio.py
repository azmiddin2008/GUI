from tkinter import *

root =Tk()
root.title("radio") 
telefon=StringVar()
telefon.set("1")
tel=StringVar()
tel.set("1")


yozuv = Label(root,text=" 1:  Birinchi mashinani kim ixtiro qilga",fg="green")
yozuv.pack()
button = Radiobutton(root,text="A: Messi",variable=telefon,value="1",fg="red")
button.pack(anchor=W)
button1 = Radiobutton(root,text="B: Ronaldo",variable=telefon,value="2",fg="red")
button1.pack(anchor=W)
button2 = Radiobutton(root,text="C: Bilmadim",variable=telefon,value="3",fg="red")
button2.pack(anchor=W)
button3 = Radiobutton(root,text="D: Odam yaratganda",variable=telefon,value="4",fg="red")
button3.pack(anchor=W)


yoz = Label(root,text="2: 12 * 6 = nechchi boladi ",fg="green")
yoz.pack()
butto = Radiobutton(root,text="A: 70",variable=tel,value="1",fg="blue")
butto.pack(anchor=W)
butt = Radiobutton(root,text="B: 66",variable=tel,value="2",fg="blue")
butt.pack(anchor=W)
but = Radiobutton(root,text="C: 72",variable=tel,value="3",fg="blue")
but.pack(anchor=W)
bu = Radiobutton(root,text="D: bilmadim",variable=tel,value="4",fg="blue")
bu.pack(anchor=W)







root.mainloop()