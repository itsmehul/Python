from tkinter import *
import mysql.connector as mysql
conn=mysql.connect(user="root",password="root",host="localhost")
cursor=conn.cursor()
cursor.execute('use library')
def showbooks():
    sql="select * from books where "+var.get()+"='"+e.get()+"'"
    cursor.execute(sql)
    results=cursor.fetchall()
    lb=Listbox(win)
    lb.grid(row=4,column=1,columnspan=2)
    for row in results:
        lb.insert(END,row)

win=Tk()
var=StringVar()
e=Entry(win)
e.grid(row=1,column=2)
r1=Radiobutton(win,text="Search by name",variable=var,value="name")
r1.grid(row=2,column=2)
r2=Radiobutton(win,text="Search by author",variable=var,value="author")
r2.grid(row=3,column=2)

b2=Button(win,text='show books',command=showbooks).grid(row=2,column=1)
mainloop()
