from tkinter import *
import mysql.connector as mysql
conn=mysql.connect(user="root",password="root",host="localhost")
cursor=conn.cursor()
cursor.execute('use library')
def ins():
    sql="insert into books values('"+name.get()+"','"+author.get()+"',"+year.get()+")"
    cursor.execute(sql)
    conn.commit()
    name.delete(0,END)
    author.delete(0,END)
    year.delete(0,END)
    messagebox.showinfo('Confirmation','record was inserted')

def showbooks():
    sql="select * from books"
    cursor.execute(sql)
    results=cursor.fetchall()
    lb=Listbox(win)
    lb.grid(row=4,column=1,columnspan=2)
    for row in results:
        lb.insert(END,row)

win=Tk()
name=Entry(win)
name.grid(row=1,column=2)
author=Entry(win)
author.grid(row=2,column=2)
year=Entry(win)
year.grid(row=3,column=2)
b1=Button(win,text='insert',command=ins).grid(row=1,column=1)
b2=Button(win,text='show books',command=showbooks).grid(row=2,column=1)
mainloop()
