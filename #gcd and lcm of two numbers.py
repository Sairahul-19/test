#gcd and lcm of two numbers

a=int(input('enter a number'))
b=int(input('enter a number'))

if a>b:
    g=a
else:
    g=b

while(True):
    if ((g%a==0) and (g%b==0)):
         lcm=g
         break
    g+=1

print(lcm) 

gcd=(a*b)//lcm
print(gcd)


