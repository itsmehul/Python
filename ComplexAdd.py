class Complex:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return self.x+other.x,self.y+other.y

    
c1=Complex(4,2)
c2=Complex(4,2)
print(c1+c2)
        
