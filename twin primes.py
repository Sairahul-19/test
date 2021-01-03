#twin primes

s=int(input('enter the number'))
e=int(input('enter the number'))

def is_prime(n):
    for i in range(2,n):
         if (n%i==0):
            return False
    return True

for i in range(s,e):
    j=i+2
    if(is_prime(i) and is_prime(j)):
        print(i,'and',j)
               

