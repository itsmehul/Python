from tkinter import *

def show_entry_fields():
   print("First Name: %s\nLast Name: %s\nAge: %s\nHeight: %s\nWeight: %s\nBlood Group: %s" % (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
Label(master, text="Age").grid(row=2)
Label(master, text="Height").grid(row=3)
Label(master, text="Weight").grid(row=4)
Label(master, text="Blood group").grid(row=5)

e1 = Entry(master).grid(row=0, column=1)
e2 = Entry(master).grid(row=1, column=1)
e3 = Entry(master).grid(row=2, column=1)
e4 = Entry(master).grid(row=3, column=1)
e5 = Entry(master).grid(row=4, column=1)
e6 = Entry(master).grid(row=5, column=1)



Button(master, text='Quit', command=master.quit).grid(row=6, column=0)
Button(master, text='Show', command=show_entry_fields).grid(row=6, column=1)

mainloop( )
