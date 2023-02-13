from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Image galarey")

img_frame = LabelFrame(root,text="",padx=30,pady=50)
img_frame.pack(padx=10,pady=10)






img1 = ImageTk.PhotoImage(Image.open("images/q.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/w.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/e.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/r.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/t.jpg"))
img6 = ImageTk.PhotoImage(Image.open("images/y.jpg"))

images = [img1, img2, img3, img4, img5, img6]

status =Label(img_frame,text="img 1 of "+str(len(images)),bd=5,relief=SUNKEN,
anchor=W)
status.grid(row=2,column=0,columnspan=3)

label_img = Label(img_frame, image=img1, text="<", padx=10, pady=10)


def right(images_raqam):
    global label_img
    global button_left
    global button_right
    
    label_img.grid_forget()
    label_img = Label (img_frame, image=images[images_raqam-1])
    button_right = Button(img_frame, text=">", padx=20, pady=5,
                          bg="black", fg="white",
                         command=lambda: right(images_raqam+1))
    button_left = Button(img_frame, text="<", padx=20, pady=5,
                         bg="black", fg="white",
                          command=lambda: left(images_raqam-1))
    if images_raqam == 6:
        button_right = Button(img_frame, text=">", padx=20,
                              pady=5, bg="black", fg="white", state=DISABLED)
        
    label_img.grid(row=0, column=0, columnspan=3)
    button_left.grid(row=1, column=0)
    button_right.grid(row=1, column=2)

    status =Label(img_frame,text="img "+ str(images_raqam)+ "of "+str(len(images)),bd=5,relief=SUNKEN,
anchor=W)
    status.grid(row=2,column=0,columnspan=3)

def left(images_raqam):
    global label_img
    global button_left
    global button_right
    
    label_img.grid_forget()
    label_img = Label(img_frame, image=images[images_raqam-1])
    button_right = Button(img_frame, text=">", padx=20, pady=5,
                          bg="black", fg="white",
                         command=lambda: right(images_raqam+1))
    button_left = Button(img_frame, text="<", padx=20, pady=5,
                         bg="black", fg="white",
                          command=lambda: left(images_raqam-1))
    if images_raqam == 1:
        button_left = Button(img_frame, text="<", padx=20,
                              pady=5, bg="black", fg="white", state=DISABLED)
        
    label_img.grid(row=0, column=0, columnspan=3)
    button_left.grid(row=1, column=0)
    button_right.grid(row=1, column=2)
    status =Label(img_frame,text="img "+ str(images_raqam)+ "of "+str(len(images)),bd=5,relief=SUNKEN,
anchor=W)
    status.grid(row=2,column=0,columnspan=3)

button_left = Button(img_frame, text="<", padx=20, pady=5, bg="black", fg="white", command=lambda: left(),state=DISABLED)
button_quit = Button(img_frame, text="Exit", padx=40, pady=5, command=root.quit, bg="black", fg="white",)
button_right = Button(img_frame, text=">", padx=20, pady=5, bg="black", fg="white", command=lambda: right(2))


label_img.grid(row=0, column=0, columnspan=3)

# img_frame.pack(padx=1

button_left.grid(row=1, column=0)
button_quit.grid(row=1, column=1,)
button_right.grid(row=1, column=2)


root.mainloop()
