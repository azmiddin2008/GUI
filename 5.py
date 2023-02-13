from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
root = Tk()
root.title("Image galarey")

img_frame = LabelFrame(root,text="",padx=10,pady=10)


def click():

    
    info = messagebox.askyesno('Installation','Siz rasm kormoqchimisiz')
    
    
    
    if info ==1:
         img_frame.pack(padx=5,pady=5)
     

    else:
        img_frame.destroy()
        


img1 = ImageTk.PhotoImage(Image.open("images/q.jpg"))   
img2 = ImageTk.PhotoImage(Image.open("images/w.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/e.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/r.jpg"))
img6 = ImageTk.PhotoImage(Image.open("images/t.jpg"))
img7 = ImageTk.PhotoImage(Image.open("images/y.jpg"))
img8 = ImageTk.PhotoImage(Image.open("images/u.jpg"))
img9 = ImageTk.PhotoImage(Image.open("images/i.jpg"))
img10 = ImageTk.PhotoImage(Image.open("images/o.jpg"))
img11 = ImageTk.PhotoImage(Image.open("images/p.jpg"))
img12 = ImageTk.PhotoImage(Image.open("images/a.jpg"))
img13 = ImageTk.PhotoImage(Image.open("images/s.jpg"))
img14 = ImageTk.PhotoImage(Image.open("images/d.jpg"))
img14 = ImageTk.PhotoImage(Image.open("images/f.jpg"))
img15 = ImageTk.PhotoImage(Image.open("images/g.jpg"))
img16 = ImageTk.PhotoImage(Image.open("images/h.jpg"))
img17 = ImageTk.PhotoImage(Image.open("images/j.jpg"))
img18 = ImageTk.PhotoImage(Image.open("images/k.jpg"))
img19 = ImageTk.PhotoImage(Image.open("images/l.jpg"))
img20 = ImageTk.PhotoImage(Image.open("images/z.jpg"))
img21 = ImageTk.PhotoImage(Image.open("images/x.jpg"))
img22 = ImageTk.PhotoImage(Image.open("images/c.jpg"))
img23 = ImageTk.PhotoImage(Image.open("images/v.jpg"))
img24 = ImageTk.PhotoImage(Image.open("images/b.jpg"))
img25 = ImageTk.PhotoImage(Image.open("images/n.jpg"))
img26 = ImageTk.PhotoImage(Image.open("images/m.jpg"))
img27 = ImageTk.PhotoImage(Image.open("images/aq.jpg"))
img28 = ImageTk.PhotoImage(Image.open("images/aw.jpg"))
img29 = ImageTk.PhotoImage(Image.open("images/ae.jpg"))
img30 = ImageTk.PhotoImage(Image.open("images/ar.jpg"))
img31 = ImageTk.PhotoImage(Image.open("images/at.jpg"))
img32 = ImageTk.PhotoImage(Image.open("images/ay.jpg"))
img33 = ImageTk.PhotoImage(Image.open("images/au.jpg"))
img34 = ImageTk.PhotoImage(Image.open("images/ai.jpg"))
img35 = ImageTk.PhotoImage(Image.open("images/ao.jpg"))
img36 = ImageTk.PhotoImage(Image.open("images/ap.jpg"))
img37 = ImageTk.PhotoImage(Image.open("images/aa.jpg"))
img38 = ImageTk.PhotoImage(Image.open("images/as.jpg"))
img39 = ImageTk.PhotoImage(Image.open("images/ad.jpg"))
img40 = ImageTk.PhotoImage(Image.open("images/af.jpg"))
img41 = ImageTk.PhotoImage(Image.open("images/ag.jpg"))



images =[img1,img2,img3,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14,img15,img16,img17,img18,img19,img20,img21,img22,img23,img24,img25,img26,img27,img28,img29,img30,img31,img32,img33,img34,img35,img36,img37,img38,img39,img40,img41]
img1 = Label(img_frame, image=img1)
img2=Label(img_frame, image=img2)
img3=Label(img_frame, image=img3)
img5=Label(img_frame, image=img5)
img6=Label(img_frame, image=img6)
img7=Label(img_frame, image=img7)
img8=Label(img_frame, image=img8)
img9=Label(img_frame, image=img9)
img10=Label(img_frame, image=img10)
img11=Label(img_frame, image=img11)
img12=Label(img_frame, image=img12)
img13=Label(img_frame, image=img13)
img14=Label(img_frame, image=img14)
img15=Label(img_frame, image=img15)
img16=Label(img_frame, image=img16)
img17=Label(img_frame, image=img17)
img18=Label(img_frame, image=img18)
img19=Label(img_frame, image=img19)
img20=Label(img_frame, image=img20)
img21=Label(img_frame, image=img21)
img22=Label(img_frame, image=img22)
img23=Label(img_frame, image=img23)
img24=Label(img_frame, image=img24)
img25=Label(img_frame, image=img25)
img26=Label(img_frame, image=img26)
img27=Label(img_frame, image=img27)
img28=Label(img_frame, image=img28)
img29=Label(img_frame, image=img29)
img30=Label(img_frame, image=img30)
img31=Label(img_frame, image=img31)
img32=Label(img_frame, image=img32)
img33=Label(img_frame, image=img33)
img34=Label(img_frame, image=img34)
img35=Label(img_frame, image=img35)
img36=Label(img_frame, image=img36)
img37=Label(img_frame, image=img37)
img38=Label(img_frame, image=img38)
img39=Label(img_frame, image=img39)
img40=Label(img_frame, image=img40)
img41=Label(img_frame, image=img41)


    


button = Button(img_frame, text="⚪", padx=40, pady=5, command=root.quit)
button.grid(row=9,column=3)
buttonq = Button(img_frame, text="◀", padx=40, pady=5,bg="white" )
buttonq.grid(row=9,column=1)
buttonl = Button(img_frame, text="⬜", padx=40, pady=5, )
buttonl.grid(row=9,column=5)


img1.grid(row=1,column=1)
img2.grid(row=1,column=2)
img3.grid(row=1,column=3)
img5.grid(row=1,column=4)
img6.grid(row=1,column=5)
img7.grid(row=2,column=1)
img8.grid(row=2,column=2)
img9.grid(row=2,column=3)
img10.grid(row=2,column=4)
img11.grid(row=2,column=5)
img12.grid(row=3,column=1)
img13.grid(row=3,column=2)
img14.grid(row=3,column=3)
img15.grid(row=3,column=4)
img16.grid(row=3,column=5)
img17.grid(row=4,column=1)
img18.grid(row=4,column=2)
img19.grid(row=4,column=3)
img20.grid(row=4,column=4)
img21.grid(row=4,column=5)
img22.grid(row=5,column=1)
img23.grid(row=5,column=2)
img24.grid(row=5,column=3)
img25.grid(row=5,column=4)
img26.grid(row=5,column=5)
img27.grid(row=6,column=1)
img28.grid(row=6,column=2)
img29.grid(row=6,column=3)
img30.grid(row=6,column=4)
img31.grid(row=6,column=5)
img32.grid(row=7,column=1)
img33.grid(row=7,column=2)
img34.grid(row=7,column=3)
img35.grid(row=7,column=4)
img36.grid(row=7,column=5)
img37.grid(row=8,column=1)
img38.grid(row=8,column=2)
img39.grid(row=8,column=3)
img40.grid(row=8,column=4)
img41.grid(row=8,column=5)


Button(root,text="Message",command=click,bg="green",fg='white').pack()


root.mainloop()
