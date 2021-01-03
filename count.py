#count of given number

n=int(input('enter the number'))
i=0
sum=0
while (n!=0):
   # i=i+1
    d=n%10       

    n=(n//10)
    sum=sum+d

print('the sum is',sum)


#print('the count of',n,'is',len(n))
