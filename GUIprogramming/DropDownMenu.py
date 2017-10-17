from tkinter import*
def doNothing():
    print("okok I won't")

root=Tk()

menu=Menu(root)
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Now Project..", command=doNothing)
subMenu.add_command(label="Now..", command=doNothing)

subMenu.add_command(label="Exit", command=doNothing)

editMenu=Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()
