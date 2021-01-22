from  tkinter import *
from tkinter import scrolledtext
def hinh():
    label5=input()
    label4.config(text=label5)
    

window = Tk() #biến tự đặt tên là window
window.title("Trợ lý ảo")
label4=Label(window,text="sssscccc")
label4.pack()
window.after(1000,hinh) 
window.mainloop()