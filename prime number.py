#prime number
prime=[]
u=int(input('enter the number'))
for n in range(2,u+1):
  if(n>1):
    for i in range(2,n):
        if (n%i==0):
          break
    else:
      prime.append(n)
print(prime)

for i in prime:
  j=i+2
  if(j in prime):
    print(i,'and',j)
