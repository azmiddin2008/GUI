from tkinter import *
root =Tk()
root.title('Dropdavn')

week =[
    'Dushanba',
    'Seshanba',
    'Chorshanba',
    'Payshanba',
    'Jumo',
    'Shanba',
    'Yakshanba'

]
def click():
    label = Label(root,text=week)
    label.pack()



var =StringVar()
var.set(week[0])

drop =OptionMenu(root, var,*week)
drop.pack()

button =Button(root,text='show',command=click,bg='black',fg='white')
button.pack() 

root.mainloop()