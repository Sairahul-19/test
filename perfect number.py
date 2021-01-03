#perfect number

a=int(input('enter the number'))
s=0
for i in range(1,a):
    rem=a%i
    if(rem==0):
        s=s+i

if(s==a):
    print('the number is perfect')
else:
    print('the number is not a perfect number')  