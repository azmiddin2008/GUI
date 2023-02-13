# canculyatr yasash
from tkinter import *

root= Tk()
root.title("Canculyatr")







entry = Entry(root, text ='',width=40,borderwidth=5)
entry.grid(row=0,column=0,columnspan=3)
def button_click(number):
    qiymat =entry.get()
    entry.delete(0,END)
    entry.insert(0,str(qiymat) + str(number))

def button_clear():
    entry.delete(0,END)


def button_add():
    birinchi_raqam= entry.get()
    global f_num
    global math
    math ='qoshuv'
    f_num =int(birinchi_raqam)
    entry.delete(0,END)

def button_minus():
    uchinchi_raqam=entry.get()
    global f_num
    global math
    math='ayru'
    f_num =int(uchinchi_raqam)
    entry.delete(0,END)

def button_kopaytru():
    tortinchi_raqam=entry.get()
    global f_num
    global math
    math='kopaytru'
    f_num =int(tortinchi_raqam)
    entry.delete(0,END)
def button_bolu():
    beshinchi_raqam=entry.get()
    global f_num
    global math
    math='bolu'
    f_num =int(beshinchi_raqam)
    entry.delete(0,END)
def button_equal():
    ikkinchi_raqam =entry.get()
    uchinchi_raqam =entry.get()
    tortinchi_raqam =entry.get()
    beshinchi_raqam =entry.get()
    entry.delete(0,END)
    
    
    if math == 'qoshuv':
        entry.insert(0,f_num +int(ikkinchi_raqam))
    elif math == "ayru":
        entry.insert(0, f_num -int(uchinchi_raqam))
    elif math == "kopaytru":
        entry.insert(0, f_num *int(tortinchi_raqam))
    elif math == "bolu":
        entry.insert(0, f_num /int(beshinchi_raqam))
    else:
        return False
button_1 =Button(root,text="1",padx=40,pady=20,command=lambda: button_click("1"))
button_2 =Button(root,text="2",padx=40,pady=20,command=lambda: button_click("2"))
button_3 =Button(root,text="3",padx=40,pady=20,command=lambda: button_click("3"))
button_4 =Button(root,text="4",padx=40,pady=20,command=lambda: button_click("4"))
button_5 =Button(root,text="5",padx=40,pady=20,command=lambda: button_click("5"))
button_6 =Button(root,text="6",padx=40,pady=20,command=lambda: button_click("6"))
button_7 =Button(root,text="7",padx=40,pady=20,command=lambda: button_click("7"))
button_8 =Button(root,text="8",padx=40,pady=20,command=lambda: button_click("8"))
button_9 =Button(root,text="9",padx=40,pady=20,command=lambda: button_click("9"))
button_0 =Button(root,text="0",padx=40,pady=20,command=lambda: button_click("0"))

button_clear =Button(root,text='Clear',padx=77,pady=20,command=button_clear)
button_add =Button(root,text="+",padx=39,pady=20,command=button_add)
button_equal =Button(root,text="=",padx=86,pady=20,command=button_equal)
button_minus =Button(root,text="-",padx=40,pady=20,command=button_minus)
button_kopaytru =Button(root,text="*",padx=40,pady=20,command=button_kopaytru)
button_bolu =Button(root,text="/",padx=40,pady=20,command=button_bolu)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)


button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)


button_0.grid(row=4,column=0)

button_clear.grid(row=4,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)



button_minus.grid(row=6,column=0)
button_kopaytru.grid(row=6,column=1)
button_bolu.grid(row=6,column=2)










root.mainloop()