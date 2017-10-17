from tkinter import *
win=Tk()

def add():
    s=int(e1.get())+int(e2.get())
    messagebox.showinfo('result',s)
def mult():
    s=int(e1.get())*int(e2.get())
    messagebox.showinfo('result',s)
def div():
    s=int(e1.get())/int(e2.get())
    messagebox.showinfo('result',s)

e1=Entry(win)
e1.pack()
e2=Entry(win)
e2.pack()
b1=Button(win,text='+',command=add).pack()
b2=Button(win,text='*',command=mult).pack()
b3=Button(win,text='/',command=div).pack()
mainloop()
