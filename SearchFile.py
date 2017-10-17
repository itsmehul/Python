a=input('enter character to find')
f=open('D:/Projects/PythonProjects/abc.txt')

x=f.read()
print(x.count(a,0,-1))
    
