a={1:3,2:1,3:7,4:8}
x=0
for i in a:
     x=x+a.get(i)   
print(x)


print(sorted(a.values()))
print(sorted(a.values(),reverse=True))

