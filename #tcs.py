#tcs.py
from sys import getsizeof
l=[11,22,33,44,55]
# # l1=l
# l2=l.copy()
# print('address of l is',id(l))
# print('address of l1 is',id(l1))
# print('address of l2 is',id(l2))
# #s=l[2:4]
# #s[0]=23
# l[3]=77
# print(l1)
# print(l)
# print(l2)
# print('the size of l',l.__sizeof__())
print(getsizeof(l))

##program for printing twin primes upto 10000

# prime=[]
# s=[]
# for n in range(2,10000):
#   if(n>1):
#     for i in range(2,n):
#         if (n%i==0):
#           break
#     else:
#       prime.append(n)

# for i in prime:
#   j=i+2
#   if(j in prime):
#     print(i,'and',j, ',',end="",)

# prime=[]
# for n in range(2,30):
#   if(n>1):
#     if (n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0):         
#       prime.append(n) 
# print(prime)         

# a=10
# print(getsizeof(a))
# d=[]
# print(getsizeof(d))

# for i in range(9):
#   d.append(i)
#   print('d[{0:3}]= {1:4}',format(i,getsizeof(d)))
#   print(d)

# import array as arr 
# a=arr.array(i,[1,2,3,4,5])
# print(a)
# print(getsizeof(a))


