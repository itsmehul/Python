from tkinter import *
from tkinter.scrolledtext import ScrolledText
root=Tk()
text=Text(root,font=('Verdana',16),height=6, width=40)
scroll=ScrolledText(root)
text.pack()
scroll.pack()
mainloop()
