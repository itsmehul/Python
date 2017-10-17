def primeno(a):
    n=2
    prm=True
    while(n<a):
        if(a%n==0):
            prm=False
        n=n+1
    return prm

a=int(input('Enter no.'))
if(primeno(a)):
    print('number is prime')
else:
    print('number is not prime')
