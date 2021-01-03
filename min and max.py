
a=input('enter the number')
b=input('enter the number')
c=input('enter the number')

if(a<b and a<c):
    print('a is minimum')
elif (b<c and b<a):
    print('the b is minimum')
else:
    print('the c is minimum') 

if(a>b and a>c):
    print('a is maximum')
elif (b>c and b>a):
    print('the b is maximum')
else:
    print('the c is maximum')        