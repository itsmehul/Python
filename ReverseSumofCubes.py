a=0
n=324
while(n>0):
    r=n%10
    a=(r**3)+a*10
    n=n//10
print(a)
