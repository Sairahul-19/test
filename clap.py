#Program to replace elements in an array with "clap" 
"""Input : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
Output: 1 2 clap 4 5 clap 7 8 clap 10 11 12 clap 14 15 clap 17 18 clap 20
n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(i+1)
    if ('3' in str(a[i]) or '6' in str(a[i]) or '9' in str(a[i])):
        b.append("clap")
    elif int(a[i])%3==0:
        b.append("clap")
    else:
        b.append(i+1) 

print(b)        


    
#program to print the following format depending on the value of n
#I/p
#n=2
#O/p
#2 2 2
#2 1 2
#2 2 2
n=int(input())
for i in range(n+1):
    a=[]
    for j in range(n+1):
        if i==1 and j==1:
            a.append(1)
        else:
            a.append(n)

    print(a)                



#I/p
#N=3
#3 3 3 3 3
#3 2 2 2 3
#3 2 1 2 3
#3 2 2 2 3
#3 3 3 3 3
N=int(input())
for i in range(N+2):
    c=[]
    for j in range(N+2):
        if i==2 and j==2:
            c.append(1)
        elif 0<i<4 and 0<j<4:
            c.append(2)
        else:
            c.append(N)
    print(c)                

#N=5
#5 5 5 5 5 5 5 5 5 
#5 4 4 4 4 4 4 4 5 
#5 4 3 3 3 3 3 4 5 
#5 4 3 2 2 2 3 4 5 
#5 4 3 2 1 2 3 4 5 
#5 4 3 2 2 2 3 4 5 
#5 4 3 3 3 3 3 4 5 
#5 4 4 4 4 4 4 4 5 
#5 5 5 5 5 5 5 5 5"""


N=int(input())
for i in range((2*N)-1):
    d=[]
    for j in range(N+4):
        if i==N-1 and j==N-1:
            d.append(1)
        elif N-3<i<N+2 and N-3<j<N+2:
            d.append(2)
        elif N-4<i<N+3 and N-4<j<N+3:
            d.append(3)
        elif 0<i<(2*N)-2 and 0<j<(2*N)-2:
            d.append(4)        
        else:
            d.append(N)
    print(d) 

"""N=int(input())
for i in range((2*N)-1):
    d=[]
    for j in range((2*N)-1):
        if i==0 or i==2*N-2:
            print(N)
        else:
            
              print(i)
    print(d)  """            

# Python3 implementation of the approach 

N = int(input())
print("Value of N: ", N)  
for i in range(1, N + 1):  

    for j in range(1, N + 1):  

        min = i if i < j else j  
        print(N - min + 1, end = " ")  
    for j in range(N - 1, 0, -1):  
        min = i if i < j else j  
        print(N - min + 1, end = " ") 
    print() 
for i in range(N - 1, 0, -1):  

    for j in range(1, N + 1):  

        min = i if i < j else j  

        print(N - min + 1, end = " ")  
    for j in range(N - 1, 0, -1):  

        min = i if i < j else j  

        print(N - min + 1, end = " ") 

    print()

"""
n=int(input())
q=2*n-1
u=[]
k=q//2
for i in range(n,0,-1):
    w=""
    for j in range(n,i-1,-1):
        w=w+str(j)+" "
    e=len(w)//2
    for r in range(0,k-e):
            w=w+str(j)+" "
    print(w,end="")
    t=w[0:len(w)-3]
    if j==1:
        print(t[::-1])
        u.append(w+t[::-1])
    else:
        print(i,end="")
        print(w[::-1])
        u.append(w+str(i)+w[::-1])
for i in range(len(u)-2,-1,-1):
    print(u[i])"""