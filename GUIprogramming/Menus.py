from tkinter import *

def swap():
    if v.get():
        e.pack_forget()
        mb.pack()
        l2.configure(text='use menu below')
    else:
        mb.pack_forget()
        e.pack()
        l2.configure(text='use entry box below')

t=Tk()
t.title('Toggle Menu')
v=IntVar()
c=Checkbutton(t,command=swap,text='select to use menu',variable=v)
c.pack()
f=Frame(t)
l2=Label(f,text='use entry box below')
l2.pack()
f.pack(side='left')
e=Entry(f)
mb=Menubutton(f,text='veg',relief='sunken')
m=Menu(mb)
mb.configure(menu=m)

for s in 'veg nonveg chinese french'.split():
    m.add_command(label=s,command=lambda s=s:mb.configure(text=s))
f.pack()
swap()
b=Button(t,text='place order',command='btclick')
b.pack()
mainloop()
        
