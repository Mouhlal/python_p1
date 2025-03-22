import json
from tkinter import *
from tkinter import ttk
with open("pays.json") as F:
    D = json.load(F)
def work(event):
    for c,v in D.items():
        if a.get() ==c:
            b.set(v)
window = Tk()
a = StringVar()
b = StringVar()
window.config(bg="powderblue")
window.geometry("500x400")
window.resizable(False,False)
tit = Label(window,text="Countries",font=('tahoma',21),fg="yellowgreen").pack(side=TOP)
lab1 = Label(window,text="Choose :",font=('tahoma',11)).place(x=100,y=150)
cmb = ttk.Combobox(window,textvariable=a)
cmb.place(x=200,y=150)
cmb['values'] = [c for c,v in D.items()]
cmb.bind('<<ComboboxSelected>>', work)

lab = Label(window,textvariable=b,font=('tahoma',11),bg="black").place(x=200,y=250)
window.mainloop()