from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
win=Tk()
pay = []
with open("p.json") as F:
        D = json.load(F)
        for d in D:
            pay.append(d["country"])
def cap(event):
    for d in D :
        if a.get()==d["country"] :
            b.set(f'{d["capitale"]}')
            c.set(f'{d["population"]}')
def nv():
    a.set("")
    b.set("")
    c.set("")
    cbo.focus()
def q():
    fk=messagebox.askyesno("Confirmation","want to leave?")
    if fk==YES:
        win.destroy()
def help(event=None):
    messagebox.showinfo("Information","this script helps u to know the capitals of countries")
a=StringVar(win)
b=StringVar(win)
c=StringVar(win)
win.title("Les Capitale des payes")
win.geometry("500x400")
win.resizable(False,False)
win.config(bg="#EBCFB2")
s=ttk.Style(win)
#s.configure("TLabel",background="#EBCFB2")
Lbl1=ttk.Label(win,text="Choisisser une pays :").place(x=50,y=100)
Lbl2=ttk.Label(win,text="Capitale :").place(x=50,y=150)
Lbl3=ttk.Label(win,text="Population :").place(x=50,y=200)
cbo=ttk.Combobox(win,state='readonl',textvariable=a,values=(pay[0],pay[1],pay[2]))
cbo.bind('<<ComboboxSelected>>',cap)
cbo.place(x=200,y=100)
txt1=ttk.Entry(win,justify=CENTER,textvariable=b).place(x=200,y=150)
txt2=ttk.Entry(win,justify=CENTER,textvariable=c).place(x=200,y=200)
btn1=ttk.Button(win,text="New",command=nv).place(x=100,y=250)
btn2=ttk.Button(win,text="Quitter",command=q).place(x=200,y=250)
btn3=ttk.Button(win,text="About",command=help).place(x=300,y=250)
win.bind('<F2>',help)
win.mainloop()


